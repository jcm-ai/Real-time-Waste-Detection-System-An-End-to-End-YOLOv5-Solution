ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1GIcOBh6M5sWGSl9MsOZYXI9zDf_iTagf/view?usp=sharing"

"""
Data validation-related constants.
All constants prefixed with DATA_VALIDATION_ for clarity.
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

# File to store validation status
DATA_VALIDATION_STATUS_FILE: str = "status.txt"

# Expected files for a valid dataset
DATA_VALIDATION_REQUIRED_FILES: list[str] = ["train", "valid", "data.yaml"]
