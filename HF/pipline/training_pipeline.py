import sys
import logging

from HF.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig
from HF.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from HF.components.data_ingestion import DataIngestion
from HF.components.data_validation import DataValidation
from HF.exception import HFException


class TrainPipeline:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_config = DataIngestionConfig()
        self.data_ingestion = DataIngestion(self.data_ingestion_config)
        self.data_validation_config = DataValidationConfig()  # Ensure proper initialization

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method starts the data ingestion process and returns the artifact.
        """
        try:
            data_ingestion_artifact = self.data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise HFException(e, sys)

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method starts the data validation process.
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
            raise HFException(e, sys) from e

    def run_pipeline(self):
        """
        Runs the entire ML pipeline from data ingestion to validation.
        """
        try:
            # Step 1: Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            
            # Step 2: Data Validation
            self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
            logging.info("Pipeline execution completed successfully.")

        except Exception as e:
            raise HFException(e, sys)
