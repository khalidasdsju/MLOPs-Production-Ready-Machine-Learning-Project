# HF/entity/artifact_entity.py
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path: str  # Path to the feature store
    training_file_path: str      # Path to the training data
    testing_file_path: str       # Path to the testing data
