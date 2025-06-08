from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionArtifact:
    """
    Artifact representing the result of the data ingestion process.
    Stores the path to the downloaded and extracted dataset.
    """
    data_zip_file_path: str
    feature_store_path: str

@dataclass(frozen=True)
class DataValidationArtifact:
    """
    Artifact representing the outcome of data validation.
    Indicates whether all required files and structure are present.
    """
    validation_status: bool

@dataclass(frozen=True)
class ModelTrainerArtifact:
    """
    Artifact returned after model training is completed.
    Stores the path to the final trained model file.
    This is immutable to ensure consistency across the pipeline.
    """
    trained_model_file_path: str
