from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your saved model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Placement model is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    cgpa = float(data["cgpa"])
    iq = float(data["iq"])

    prediction = model.predict([[cgpa, iq]])[0]

    return jsonify({"placement_prediction": int(prediction)})

if __name__ == "__main__":
    app.run()
