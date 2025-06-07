from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str
