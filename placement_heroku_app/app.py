import pickle
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Load model + scaler safely ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)

model = data["model"]
scaler = data["scaler"]

@app.route("/")
def home():
    return "Placement model is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    cgpa = float(data["cgpa"])
    iq = float(data["iq"])

    # Scale input
    scaled = scaler.transform([[cgpa, iq]])

    prediction = model.predict(scaled)[0]

    return jsonify({"placement_prediction": int(prediction)})

if __name__ == "__main__":
    app.run()
