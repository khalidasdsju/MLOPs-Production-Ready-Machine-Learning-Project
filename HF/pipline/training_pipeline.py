import sys
import logging

from HF.entity.config_entity import (
    TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, DataTransformationConfig
)
from HF.entity.artifact_entity import (
    DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
)
from HF.components.data_ingestion import DataIngestion
from HF.components.data_validation import DataValidation
from HF.components.data_transformation import DataTransformation
from HF.exception import HFException


class TrainPipeline:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_config = DataIngestionConfig()
        self.data_ingestion = DataIngestion(self.data_ingestion_config)
        self.data_validation_config = DataValidationConfig()
        self.data_transformation_config = DataTransformationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Starts the data ingestion process and returns the artifact.
        """
        try:
            logging.info("Starting data ingestion...")
            data_ingestion_artifact = self.data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed successfully.")
            return data_ingestion_artifact
        except Exception as e:
            raise HFException(e, sys)

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        Starts the data validation process.
        """
        try:
            logging.info("Starting data validation...")
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Data validation completed successfully.")
            return data_validation_artifact
        except Exception as e:
            raise HFException(e, sys)

    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        """
        Starts the data transformation process.
        """
        try:
            logging.info("Starting data transformation...")
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config,
                data_validation_artifact=data_validation_artifact
            )
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info("Data transformation completed successfully.")
            return data_transformation_artifact
        except Exception as e:
            raise HFException(e, sys)

    def run_pipeline(self):
        """
        Runs the entire ML pipeline from data ingestion to transformation.
        """
        try:
            logging.info("Pipeline execution started.")
            
            # Step 1: Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            
            # Step 2: Data Validation
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            
            # Step 3: Data Transformation
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact, data_validation_artifact
            )
            
            logging.info("Pipeline execution completed successfully.")
        except Exception as e:
            raise HFException(e, sys)
