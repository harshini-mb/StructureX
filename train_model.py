import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# 1. Generate realistic synthetic structural failure data
np.random.seed(42)
N = 3000

age = np.random.uniform(1, 100, N)               # 1 to 100 years
crack = np.random.uniform(0.1, 25.0, N)          # 0.1 to 25 mm
vibration = np.random.uniform(5.0, 100.0, N)     # 5 to 100 Hz
stress = np.random.uniform(20.0, 160.0, N)       # 20 to 160 %
weather = np.random.randint(1, 11, N)            # 1 to 10 scale
maintenance = np.random.randint(1, 11, N)        # 1 to 10 scale

# Structural Risk Index Formula (ground truth generation)
risk_index = (
    0.20 * (age / 100) +
    0.25 * (crack / 25) +
    0.15 * (vibration / 100) +
    0.25 * (stress / 160) +
    0.15 * (weather / 10) -
    0.20 * (maintenance / 10)
)

# Label: 1 = High Risk/Failure, 0 = Safe
y = (risk_index > 0.48).astype(int)

X = pd.DataFrame({
    'age': age,
    'crack_width': crack,
    'vibration': vibration,
    'load_stress': stress,
    'weather': weather,
    'maintenance': maintenance
})

# 2. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train Classifier
model = RandomForestClassifier(n_estimators=120, max_depth=8, random_state=42)
model.fit(X_scaled, y)

# 4. Save trained model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ Model & Scaler successfully saved as model.pkl and scaler.pkl")
