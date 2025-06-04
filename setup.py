from setuptools import setup, find_packages

setup(
    name="wasteDetection",
    version="0.0.1",
    author="Jagadish Mali",
    description="This project develops an automated waste detection system using YOLOv5 deep learning and computer vision. It accurately identifies and classifies waste in real time from images and video, aiming to significantly boost waste management efficiency and support smart city environmental initiatives.",
    long_description=open("README.md").read(),
    author_email="jagadishmali567@gmail.com",
    packages=find_packages(),
    install_requires=[]
)