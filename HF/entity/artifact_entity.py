
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path: str  # Path to the feature store
    training_file_path: str      # Path to the training data
    testing_file_path: str       # Path to the testing data

###########################################################################

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str
############################################################################
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str