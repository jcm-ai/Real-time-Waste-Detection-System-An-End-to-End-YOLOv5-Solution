from wasteDetection.logger import logging
from wasteDetection.exception import AppException
import sys

try:
    a = 1 / "0"
except Exception as e:
    logging.info("Divide by zero error")
    raise AppException(e, sys) from e