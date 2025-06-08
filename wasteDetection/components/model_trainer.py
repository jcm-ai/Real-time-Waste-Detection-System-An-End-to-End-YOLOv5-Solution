import os
import sys
import yaml
import shutil
import subprocess
from wasteDetection.utils.main_utils import read_yaml_file
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import ModelTrainerConfig
from wasteDetection.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    """
    Trains a YOLOv5 model using custom configuration and dataset.
    Handles configuration updates, training execution, and model artifact saving.
    """

    def __init__(self, model_trainer_config: ModelTrainerConfig):
        """
        Initializes the ModelTrainer with the given configuration.
        """
        self.model_trainer_config = model_trainer_config

    def _prepare_model_config(self, num_classes: int, base_model: str) -> str:
        """
        Reads and updates the base model config to reflect the number of custom classes.
        Returns the path to the new custom config file.
        """
        try:
            config_path = os.path.join("yolov5", "models", f"{base_model}.yaml")
            config = read_yaml_file(config_path)
            config["nc"] = num_classes  # update number of classes

            custom_config_path = os.path.join("yolov5", "models", f"custom_{base_model}.yaml")
            with open(custom_config_path, "w") as f:
                yaml.dump(config, f)

            return custom_config_path
        except Exception as e:
            raise AppException(e, sys)

    def _clean_up(self):
        """
        Deletes temporary files and folders after training.
        """
        for item in ["train", "valid", "data.yaml", "data.zip", "yolov5/runs"]:
            if os.path.exists(item):
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
        # Step 1: Unzip the dataset
            if os.path.exists("data.zip"):
                os.system("unzip data.zip")
                os.remove("data.zip")

        # Step 2: Read number of classes from data.yaml
            with open("data.yaml", 'r') as f:
                num_classes = yaml.safe_load(f).get("nc", 0)

            base_model = self.model_trainer_config.weight_name.split(".")[0]
            original_cfg_path = os.path.join("yolov5", "models", f"{base_model}.yaml")
            custom_cfg_path = os.path.join("yolov5", "models", f"custom_{base_model}.yaml")

            # Step 3: Load and modify the config file
            config = read_yaml_file(original_cfg_path)
            config["nc"] = num_classes
            with open(custom_cfg_path, "w") as f:
                yaml.dump(config, f)

            # Step 4: Train the model
            train_cmd = [
                "python", "train.py",
                "--img", "416",
                "--batch", str(self.model_trainer_config.batch_size),
                "--epochs", str(self.model_trainer_config.no_epochs),
                "--data", "../data.yaml",
                "--cfg", f"models/custom_{base_model}.yaml",  # relative to yolov5/
                "--weights", self.model_trainer_config.weight_name,
                "--name", "yolov5s_results",
                "--cache"
            ]

            logging.info(f"Running training command: {' '.join(train_cmd)}")
            subprocess.run(train_cmd, cwd="yolov5", check=True)

            # Step 5: Move best.pt to final model location
            trained_model_src = os.path.join("yolov5", "runs", "train", "yolov5s_results", "weights", "best.pt")
            trained_model_dst = os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy(trained_model_src, trained_model_dst)
            shutil.copy(trained_model_src, os.path.join("yolov5", "best.pt"))

            # Step 6: Clean up
            self._clean_up()

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=os.path.join("yolov5", "best.pt")
            )

            logging.info(f"Model trainer artifact created at: {model_trainer_artifact.trained_model_file_path}")
            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)