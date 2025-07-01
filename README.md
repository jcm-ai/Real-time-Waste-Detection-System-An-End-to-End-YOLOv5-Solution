# Real-time Waste Detection System: An End-to-End YOLOv5 Solution
This is a real-time waste detection system, which uses YOLOv5 for object detection. It is a complete solution that includes training and deployment. The system is built using Python, PyTorch, and YOLOv5. It allows users to upload images or videos for waste detection, and the system will provide real-time results.

**Final outcome of this project:**

![waste_detection](https://github.com/user-attachments/assets/e8d7736a-3cb0-47ef-8721-512b00905b09)

## Problem Statement:
*The escalating global waste crisis poses significant environmental, economic, and public health challenges. Traditional waste management practices often struggle with inefficient collection, sorting, and recycling processes, leading to overflowing landfills, increased pollution, and valuable resource depletion. A key bottleneck in optimizing these processes is the lack of a real-time, accurate, and automated system for identifying and categorizing different types of waste.*

*Current methods frequently rely on manual inspection, which is labor-intensive, prone to human error, and lacks the speed required for large-scale operations. While some automated systems exist, many are limited by their inability to operate in diverse, real-world conditions, differentiate between various waste materials effectively, or provide instant feedback for immediate action. This deficiency hinders efforts to implement smart waste bins, automate sorting facilities, and monitor illegal dumping, ultimately slowing down progress towards sustainable waste management.*


### Project Workflow:

1. **constant**: Define constants and configurations for the project.
2. **entity**: Define entities for the project.
3. **components**: Define components for the project.
4. **pipeline**: Define the pipeline for the project.
5. **app_gradio.py**: Define the main function for the project.

### How to run the project:
**clone the repository:**
```bash
git clone https://github.com/jcm-ai/Real-time-Waste-Detection-System-An-End-to-End-YOLOv5-Solution.git
```
**Create a virtual environment or conda environment after cloning the repository**
```bash
conda create --name waste python=3.10 -y
```
*Incase if you get error (for example: CondaError: Run 'conda init' before 'conda activate') when activate environment, use below command:*
```bash
source activate base
```
**Then, Activate an environment:**
```bash
conda activate waste
```
**Install the required packages Install the required packages using pip or conda. For example, to install the required packages using pip , run the following command:**
```bash
pip install -r requirements.txt
```
## Streamlining AWS Deployments with GitHub Actions CI/CD
### 1. Login to AWS console
### 2. Set up an IAM user for deployments
Policy:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

*With this policy, we can deploy Docker images to Amazon Elastic Container Registry (ECR).*
Description: About the deployments
1. Build Docker image from source code
2. Push Docker image to Amazon ECR (Amazon Elastic Container Registry)
3. Create an EC2 instance
3. Run the Docker image on the EC2 instance
4. Deploy Docker image to AWS EC2 (Amazon Elastic Compute Cloud)

### 3. Creating an ECR Repository for Docker Image Storage
```bash
AWS ECR Repo URI: 954976285001.dkr.ecr.ap-south-1.amazonaws.com/waste
```
### 4. Creating an Ubuntu EC2 Instance or Machine
### 5. Step-by-Step: Installing Docker on AWS EC2:
Optional: Install Docker on AWS EC2
```bash
sudo apt-get update -y
```
```bash
sudo apt-get upgrade
```
Required: Install Docker on AWS EC2
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
```bash
sudo sh get-docker.sh
```
```bash
sudo usermod -aG docker ubuntu
```
```bash
newgrp docker
```

### 6. Configure EC2 as self-hosted runner:
```bash
Settings>Actions>Runners>New self-hosted runner> choose os> then run command one by one
```

### 7. Setup GitHub secrets:
```bash
Settings>Secrets and variables>Actions>New repository secret
```
AWS_ACCESS_KEY_ID = ***********************************

AWS_SECRET_ACCESS_KEY = ***********************************

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = 954976285001.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = waste
