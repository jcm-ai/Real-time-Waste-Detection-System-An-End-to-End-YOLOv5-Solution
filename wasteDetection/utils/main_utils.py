import os
import sys
import yaml
import base64

from wasteDetection.exception import AppException
from wasteDetection.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info(f"Successfully read YAML file: {file_path}")
            return yaml.safe_load(yaml_file) or {}  # Ensure return is always a dict
    except Exception as e:
        raise AppException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info(f"Successfully wrote YAML file: {file_path}")
    except Exception as e:
        raise AppException(e, sys)


def decodeImage(imgstring: str, fileName: str) -> None:
    try:
        os.makedirs("./data", exist_ok=True)  # Ensure directory exists
        imgdata = base64.b64decode(imgstring)
        with open(os.path.join("data", fileName), 'wb') as f:
            f.write(imgdata)
        logging.info(f"Decoded and saved image to: data/{fileName}")
    except Exception as e:
        raise AppException(e, sys)


def encodeImageIntoBase64(croppedImagePath: str) -> str:
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")  # Return as UTF-8 string
    except Exception as e:
        raise AppException(e, sys)
