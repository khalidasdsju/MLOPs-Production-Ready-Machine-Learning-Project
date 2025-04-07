from HF.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from HF.components.data_ingestion import DataIngestion
from HF.exception import HFException
import sys

class TrainPipeline:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_config = DataIngestionConfig()  # Make sure you import and use your config properly
        self.data_ingestion = DataIngestion(self.data_ingestion_config)

    def start_data_ingestion(self):
        try:
            data_ingestion_artifact = self.data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise HFException(e, sys)

    def run_pipeline(self):
        try:
            self.start_data_ingestion()  # Start with data ingestion
            # You can add more steps for other stages of the pipeline, e.g., data validation, transformation, etc.
        except Exception as e:
            raise HFException(e, sys)
