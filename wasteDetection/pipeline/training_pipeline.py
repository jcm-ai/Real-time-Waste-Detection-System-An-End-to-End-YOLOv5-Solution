import sys
import os
from wasteDetection.logger import logging
from wasteDetection.exception import AppException

from wasteDetection.components.data_ingestion import DataIngestion
from wasteDetection.components.data_validation import DataValidation
#from wasteDetection.components.model_trainer import ModelTrainer

from wasteDetection.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
)
from wasteDetection.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
)


class TrainPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            #self.model_trainer_config = ModelTrainerConfig()
        except Exception as e:
            raise AppException(e, sys)

    def start_data_ingestion(self) -> DataIngestionArtifact:
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

    # def start_model_trainer(self) -> ModelTrainerArtifact:
    #     try:
    #         logging.info("Starting model training...")
    #         model_trainer = ModelTrainer(self.model_trainer_config)
    #         artifact = model_trainer.initiate_model_trainer()
    #         logging.info("Completed model training.")
    #         return artifact
    #     except Exception as e:
    #         raise AppException(e, sys)

    def run_pipeline(self) -> None:
        try:
            ingestion_artifact = self.start_data_ingestion()
            validation_artifact = self.start_data_validation(data_ingestion_artifact=ingestion_artifact)

            # if validation_artifact.validation_status:
            #     self.start_model_trainer()
            # else:
            #     raise ValueError("Data validation failed. Check format and integrity.")

        except Exception as e:
            raise AppException(e, sys)
