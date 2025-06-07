from dataclasses import dataclass

@dataclass(frozen=True) # Making it immutable and hashable
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str
    
@dataclass(frozen=True)
class DataValidationArtifact:
    validation_status: bool
