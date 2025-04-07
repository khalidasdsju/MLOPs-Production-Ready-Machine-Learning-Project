import os
import sys
import pandas as pd
from pandas import DataFrame
from HF.exception import HFException
from HF.logger import logging
from HF.entity.config_entity import DataIngestionConfig
from HF.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split
from HF.data_access.Study_Data import StudyData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HFException(e, sys)
    
    def export_data_into_feature_store(self) -> DataFrame:
        # your existing code
        pass

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        # your existing code
        pass

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method initiates the data ingestion components of the training pipeline
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")

            self.split_data_as_train_test(dataframe)
            logging.info("Performed train test split on the dataset")

            # Return DataIngestionArtifact with correct paths
            data_ingestion_artifact = DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                training_file_path=self.data_ingestion_config.training_file_path,
                testing_file_path=self.data_ingestion_config.testing_file_path
            )

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise HFException(e, sys)