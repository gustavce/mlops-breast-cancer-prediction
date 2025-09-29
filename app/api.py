from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Cargar modelo
model = joblib.load("model.joblib")

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data or "input" not in data:
            logging.error("Input missing in request")
            return jsonify({"error": "Missing 'input' field"}), 400
        input_data = np.array(data["input"]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
