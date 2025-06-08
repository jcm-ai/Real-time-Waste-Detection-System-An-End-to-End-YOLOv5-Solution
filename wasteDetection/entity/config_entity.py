import os
from dataclasses import dataclass
from datetime import datetime
from wasteDetection.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    """
    Base configuration for the training pipeline.
    Stores the root directory path for all artifacts.
    """
    artifacts_dir: str = ARTIFACTS_DIR  # Base directory for storing pipeline artifacts
# Create a single instance of pipeline config to share across other configs
training_pipeline_config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion process.
    Handles download paths and storage structure.
    """
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL
    
@dataclass
class DataValidationConfig:
    """
    Configuration class for data validation.
    Includes directory path, status file, and required file checks.
    """
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_REQUIRED_FILES    

@dataclass
class ModelTrainerConfig:
    """
    Configuration class for model trainer settings.
    Stores training parameters and paths used in the training process.
    """

    # Directory to store all model trainer related files
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )

    # Name of the pre-trained YOLOv5 model weights
    weight_name: str = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    # Number of training epochs
    no_epochs: int = MODEL_TRAINER_NO_EPOCHS

    # Batch size used during training
    batch_size: int = MODEL_TRAINER_BATCH_SIZE    