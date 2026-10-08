# StructureX — AI Structural Health & Risk Predictor

StructureX is an intelligent diagnostic tool designed to evaluate structural integrity and calculate risk failure probability for civil infrastructure such as bridges, high-rise buildings, and industrial facilities.

---

## 🚀 Key Features

- **Multi-Parameter Engineering Evaluation**: Calculates failure probability using age, crack width, vibration frequency, load stress, environmental weathering, and maintenance ratings.
- **Dynamic 10-Year Degradation Forecast**: Compares future degradation risks between inaction and proactive maintenance.
- **Real-Time Inspection Log**: Chronologically records recent tests directly inside the UI.
- **Instant Printable Report**: Generates a clean, audit-ready PDF/print view.
- **Dual Runtime Support**: Runs as a standalone zero-dependency web application (`index.html`) or paired with a Python Flask machine learning backend (`app.py`).

---

## 📁 Repository Structure

```text
StructureX/
│
├── index.html          # Complete standalone Web UI & visualizer
├── train_model.py      # ML training script (Random Forest Classifier)
├── app.py              # Flask REST API server
├── requirements.txt    # Python dependencies
├── .gitignore          # Git exclusion rules
├── LICENSE             # MIT License
└── README.md           # Documentation
```

---

## ⚡ Quick Start

### Option 1: Standalone (No installation needed)
Just double-click `index.html` in any browser, or host it directly with **GitHub Pages**.

### Option 2: Run with Flask & Machine Learning
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/StructureX.git
   cd StructureX
   ```

2. Set up virtual environment and install packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train_model.py
   ```

4. Launch the server:
   ```bash
   python app.py
   ```
5. Open `http://localhost:5000` in your web browser.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
