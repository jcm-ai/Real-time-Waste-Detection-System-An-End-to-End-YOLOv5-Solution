import sys
import os
from wasteDetection.logger import logging
from wasteDetection.exception import AppException

from wasteDetection.components.data_ingestion import DataIngestion
from wasteDetection.components.data_validation import DataValidation
from wasteDetection.components.model_trainer import ModelTrainer

from wasteDetection.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    ModelTrainerConfig
)
from wasteDetection.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact
)


class TrainPipeline:
    def __init__(self):
        """
        Initializes the TrainPipeline class, setting up configurations
        for data ingestion, validation, and model training.

        Raises:
            AppException: If there is an error during initialization.
        """

        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            self.model_trainer_config = ModelTrainerConfig()
        except Exception as e:
            raise AppException(e, sys)

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process and returns the resulting artifact.

        Returns:
            DataIngestionArtifact: Contains information about the downloaded and
            extracted dataset, including the paths for the data zip file and
            feature store directory.

        Raises:
            AppException: If an error occurs during the data ingestion process.
        """

        try:
            logging.info("Starting data ingestion...")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Completed data ingestion.")
            return artifact
        except Exception as e:
            raise AppException(e, sys)

    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:
        """
        Initiates the data validation process and returns the resulting artifact.

        Args:
            data_ingestion_artifact (DataIngestionArtifact): Artifact from the data ingestion process.

        Returns:
            DataValidationArtifact: Contains information about the validation status.

        Raises:
            AppException: If an error occurs during the data validation process.
        """

        try:
            logging.info("Starting data validation...")
            data_validation = DataValidation(
                data_ingestion_artifact, self.data_validation_config
            )
            artifact = data_validation.initiate_data_validation()
            logging.info("Completed data validation.")
            return artifact
        except Exception as e:
            raise AppException(e, sys)

    def start_model_trainer(self) -> ModelTrainerArtifact:
        """
        Initiates the model training process and returns the resulting artifact.

        Returns:
            ModelTrainerArtifact: Contains information about the trained model, including the path to the final model file.

        Raises:
            AppException: If an error occurs during the model training process.
        """
        try:
            logging.info("Starting model training...")
            model_trainer = ModelTrainer(self.model_trainer_config)
            artifact = model_trainer.initiate_model_trainer()
            logging.info("Completed model training.")
            return artifact
        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self) -> None:
        """
        Executes the entire training pipeline, including data ingestion,
        validation, and model training. Begins by ingesting data, then
        validates the ingested data, and finally trains the model if
        validation is successful.

        Raises:
            AppException: If any step in the pipeline fails.
            ValueError: If data validation fails indicating issues with
            data format or integrity.
        """

        try:
            ingestion_artifact = self.start_data_ingestion()
            validation_artifact = self.start_data_validation(data_ingestion_artifact=ingestion_artifact)

            if validation_artifact.validation_status:
                self.start_model_trainer()
            else:
                raise ValueError("Data validation failed. Check format and integrity.")

        except Exception as e:
            raise AppException(e, sys)
