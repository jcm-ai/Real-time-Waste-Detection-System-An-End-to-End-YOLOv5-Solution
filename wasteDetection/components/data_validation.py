import os
import sys
import shutil
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataValidationConfig
from wasteDetection.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)


class DataValidation:
    """
    Handles validation of the data required for training.
    Ensures all required files exist in the feature store directory.
    """

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        """
        Initializes DataValidation with ingestion artifact and config.

        Args:
            data_ingestion_artifact (DataIngestionArtifact): Info about ingested data.
            data_validation_config (DataValidationConfig): Validation config parameters.
        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files_exist(self) -> bool:
        """
        Validates whether all required files are present in the feature store directory.

        Returns:
            bool: True if all required files exist, False otherwise.
        """
        try:
            logging.info("Validating presence of required files...")

            existing_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            required_files = set(self.data_validation_config.required_file_list)

            # Check if all required files exist in the feature store
            validation_status = required_files.issubset(set(existing_files))

            # Ensure the directory exists
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)

            # Write validation status to file
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logging.info(f"Validation status written: {validation_status}")
            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Executes the validation process and returns a validation artifact.

        Returns:
            DataValidationArtifact: Result of the validation process.
        """
        logging.info("Entered initiate_data_validation method of DataValidation class")

        try:
            status = self.validate_all_files_exist()

            # Prepare validation artifact
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            logging.info(f"Data validation artifact created: {data_validation_artifact}")

            # Optionally copy data.zip to current working directory if validation passed
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                logging.info("Data zip file copied to current working directory.")

            logging.info("Exited initiate_data_validation method of DataValidation class")
            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)

# This code handles data validation for a machine learning pipeline, ensuring that all required files are present in the feature store directory.