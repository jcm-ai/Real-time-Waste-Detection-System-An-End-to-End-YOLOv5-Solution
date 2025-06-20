# Use the official Python 3.10 slim-buster image as the base image.
# This image is smaller than the full Python image, which is good for production.
FROM python:3.10-slim-buster

# Set the working directory inside the container to /app_gradio.py.
# All subsequent commands will be run from this directory.
WORKDIR /app_gradio.py

# Copy the entire contents of the current directory (where the Dockerfile is located)
# into the /app_gradio.py directory inside the container.
COPY . /app_gradio.py

# Update the package list and install awscli.
# The -y flag automatically answers yes to prompts.
RUN apt update -y && apt install awscli -y

# Upgrade pip to the latest version.
# This ensures that we have the latest version of pip for installing Python packages.
RUN pip install --upgrade pip
# Update the package list, install ffmpeg, libsm6, libxext6, and unzip.
# ffmpeg is often used for media processing.
# libsm6 and libxext6 are frequently required by libraries like OpenCV.
# unzip is useful for extracting compressed files.
# Finally, install Python dependencies from requirements.txt using pip.
# --no-cache-dir prevents pip from storing cached downloads, reducing image size.
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install --no-cache-dir -r requirements.txt

# Specify the command to run when the container starts.
# This will execute the app_gradio.py script using python3.
CMD ["python3", "app_gradio.py"]