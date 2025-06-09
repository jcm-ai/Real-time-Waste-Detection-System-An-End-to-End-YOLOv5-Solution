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


"""
Constants related to the model training phase of the waste detection pipeline.
These are prefixed with MODEL_TRAINER_ to maintain clarity and modularity.
"""

# Directory name where all model trainer related artifacts will be stored
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

# Name of the pretrained YOLOv5 weights to be used for transfer learning
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

# Number of training epochs to run during model training
MODEL_TRAINER_NO_EPOCHS: int = 1 # make it 1 for testing, change it to 100-500 for actual training

# Batch size to be used during model training
MODEL_TRAINER_BATCH_SIZE: int = 16
