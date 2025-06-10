import sys
import os
import subprocess
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from wasteDetection.pipeline.training_pipeline import TrainPipeline
from wasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from wasteDetection.constant.application import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/train")
def train_route():
    """Trains the model"""
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful!!"

@app.route("/")
def home():
    """Renders the index.html template"""
    return render_template("index.html")

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict_route():
    """Predicts the output based on the input image"""
    try:
        image = request.json['image']
        decodeImage(image, ClientApp().filename)

        # Use subprocess instead of os.system for better security and control
        subprocess.run(["cd", "yolov5/", "&&", "python", "detect.py", "--weights", "best.pt", "--img", "416", "--conf", "0.5", "--source", "../data/inputImage.jpg"])

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        subprocess.run(["rm", "-rf", "yolov5/runs"])

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)

@app.route("/live", methods=['GET'])
@cross_origin()
def predict_live():
    """Predicts the output based on the live camera feed"""
    try:
        # Use subprocess instead of os.system for better security and control
        subprocess.run(["cd", "yolov5/", "&&", "python", "detect.py", "--weights", "best.pt", "--img", "416", "--conf", "0.5", "--source", "0"])
        subprocess.run(["rm", "-rf", "yolov5/runs"])
        return "Camera starting!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)