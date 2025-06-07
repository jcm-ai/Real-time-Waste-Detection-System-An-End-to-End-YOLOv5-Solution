import os
import sys
import zipfile
import gdown
from wasteDetection.exception import AppException
from wasteDetection.logger import logging
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self) -> str:
        """
        Fetch data from the URL and save as a ZIP file locally.
        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)

            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)

            logging.info(f"Downloading data from {dataset_url} to {zip_file_path}")

            file_id = dataset_url.split("/")[-2]
            gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", zip_file_path, quiet=False)

            logging.info(f"Data downloaded to {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        Extracts the ZIP file to the feature store directory.
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracted {zip_file_path} to {feature_store_path}")
            return feature_store_path

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Initiating data ingestion process...")

        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info(f"Data ingestion completed with artifact: {artifact}")
            return artifact

        except Exception as e:
            raise AppException(e, sys)
