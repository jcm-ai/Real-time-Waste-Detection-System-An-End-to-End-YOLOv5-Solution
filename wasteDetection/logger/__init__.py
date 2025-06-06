import logging
from datetime import datetime
from pathlib import Path
from from_root import from_root

# Generate log file name with timestamp
LOG_FILENAME = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"

# Construct log directory and file path
log_dir = Path(from_root()) / "log"
log_dir.mkdir(parents=True, exist_ok=True)  # Ensure the log directory exists

LOG_FILE_PATH = log_dir / LOG_FILENAME

# Configure logging
logging.basicConfig(
    filename=str(LOG_FILE_PATH),
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
