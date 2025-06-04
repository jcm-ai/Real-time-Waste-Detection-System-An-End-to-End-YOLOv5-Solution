import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define project name
PROJECT_NAME = "wasteDetection"

# List of project files and directories
files_to_create = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/constant/__init__.py",
    f"{PROJECT_NAME}/constant/training_pipeline/__init__.py",
    f"{PROJECT_NAME}/constant/application.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifacts_entity.py",
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/logger/__init__.py",
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

# Create directories and files
for file_path in files_to_create:
    path = Path(file_path)
    dir_path = path.parent

    # Create directory if it doesn't exist
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")

    # Create empty file if it doesn't exist or is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Created empty file: {path}")
    else:
        logging.info(f"File already exists and is not empty: {path}")
