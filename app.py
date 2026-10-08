from flask import Flask, render_template, request, jsonify, send_from_directory
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='.', template_folder='.')

# Load or lazy load trained model and scaler if available
model = None
scaler = None
if os.path.exists('model.pkl') and os.path.exists('scaler.pkl'):
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        age = float(data.get('age', 0))
        crack = float(data.get('crack_width', 0))
        vibration = float(data.get('vibration', 0))
        stress = float(data.get('load_stress', 0))
        weather = int(data.get('weather', 1))
        maintenance = int(data.get('maintenance', 1))

        if model is not None and scaler is not None:
            features = np.array([[age, crack, vibration, stress, weather, maintenance]])
            features_scaled = scaler.transform(features)
            prob = float(model.predict_proba(features_scaled)[0][1] * 100)
        else:
            # Fallback heuristic calculation matching UI
            score = (age * 0.18) + (crack * 1.35) + (vibration * 0.22) + (stress * 0.25) + (weather * 1.5) - (maintenance * 2.0)
            prob = float(min(99.9, max(1.0, score)))

        if prob >= 75:
            status = "HIGH RISK of Structural Failure"
            level = "high"
        elif prob >= 40:
            status = "MODERATE RISK of Deterioration"
            level = "medium"
        else:
            status = "LOW RISK: Structural Integrity Stable"
            level = "low"

        return jsonify({
            'success': True,
            'probability': f"{prob:.2f}%",
            'raw_prob': prob,
            'status': status,
            'level': level
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
