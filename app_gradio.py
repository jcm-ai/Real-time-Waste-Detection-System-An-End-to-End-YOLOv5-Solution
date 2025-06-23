import os
import uuid
import torch
import pathlib
import gradio as gr
from wasteDetection.pipeline.training_pipeline import TrainPipeline
from wasteDetection.utils.main_utils import encodeImageIntoBase64, decodeImage
from wasteDetection.constant.application import APP_HOST, APP_PORT

import subprocess
import glob
import shutil


# ---------- TRAINING FUNCTION ----------
def train_yolov5():
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        return "✅ Training completed successfully!"
    except Exception as e:
        return f"❌ Training failed: {str(e)}"


# ---------- DETECTION FUNCTION ----------
def predict_yolov5(input_image):
    try:
        import pathlib
        pathlib.PosixPath = pathlib.WindowsPath  # Patch to fix PosixPath issue on Windows

        filename = f"{uuid.uuid4().hex}.jpg"
        input_path = os.path.join("data", filename)
        input_image.save(input_path)

        subprocess.run([
            "python", "detect.py",
            "--weights", "best.pt",
            "--img", "416",
            "--conf", "0.5",
            "--source", f"../{input_path}"
        ], cwd="yolov5")

        exp_dirs = sorted(glob.glob("yolov5/runs/detect/exp*"), key=os.path.getmtime)
        latest_dir = exp_dirs[-1]
        result_path = os.path.join(latest_dir, filename)

        return result_path

    except Exception as e:
        return f"❌ Prediction failed: {str(e)}"


# ---------- GRADIO INTERFACE ----------
with gr.Blocks(title="🗑️ Waste Detection System (YOLOv5)") as app:
    gr.Markdown("## 🔍 Real-time Waste Detection System: An End-to-End YOLOv5 Solution")

    with gr.Tab("🧠 Train Model"):
        train_btn = gr.Button("🚀 Start Training")
        train_output = gr.Textbox(label="Status")
        train_btn.click(fn=train_yolov5, outputs=train_output)

    with gr.Tab("📸 Predict Image"):
        image_input = gr.Image(type="pil", label="Upload an image")
        image_output = gr.Image(label="Detection Result")
        predict_btn = gr.Button("🎯 Detect Waste")
        predict_btn.click(fn=predict_yolov5, inputs=image_input, outputs=image_output)

    gr.Markdown("---")
    gr.Markdown("Built with ❤️ using YOLOv5 and Gradio by [Jagadish Mali](https://github.com/jcm-ai)")

# Launch the Gradio app
if __name__ == "__main__":
    app.launch(server_name=APP_HOST, server_port=APP_PORT, share=True, debug=True)
