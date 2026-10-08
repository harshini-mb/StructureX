# 🏗️ StructureX — AI Structural Health & Risk Predictor


**StructureX** is a modern web-based structural health and risk assessment application designed to help engineers, facility managers, and safety inspectors evaluate potential structural failure risks using multiple structural and environmental parameters.

🔗 **Live Demo:** https://structurex-five.vercel.app/

---

## 📸 Overview

![StructureX Interface]<img width="759" height="593" alt="Screenshot 2026-10-08 183019" src="https://github.com/user-attachments/assets/36f5711f-7e4f-434b-9e47-d288160296be" />
<img width="656" height="567" alt="Screenshot 2026-10-08 183033" src="https://github.com/user-attachments/assets/f55527d7-19b6-423b-928f-bf32ff02c6c8" />



StructureX provides an interactive dashboard where users can enter structural and environmental parameters and receive a dynamically calculated **structural risk score and failure probability**.

The application is designed as a prototype for exploring how data-driven approaches can support structural inspection and preventive maintenance decisions.

---

## ✨ Key Features

### 🔍 Multi-Parameter Structural Assessment

StructureX evaluates structural conditions using multiple parameters:

* 🏢 **Age of Structure** — measured in years
* 🧱 **Crack Width** — displacement measured in millimeters
* 📳 **Vibration Level** — measured in Hz
* ⚙️ **Load Stress Capacity** — percentage of load capacity
* 🌦️ **Weather Impact Score** — scale of 1–10
* 🔧 **Maintenance History Score** — scale of 1–10

### 📊 Dynamic Risk Assessment

The application provides real-time feedback based on the entered parameters, including:

* Failure probability percentage
* Overall structural risk score
* Risk classification:

  * 🟢 Low Risk
  * 🟡 Moderate Risk
  * 🔴 High Risk

### 📈 10-Year Degradation Forecast

StructureX provides an interactive **10-year degradation forecast**, allowing users to compare:

* Expected deterioration without intervention
* Potential trajectory with proactive maintenance

### 📝 Inspection Audit Log

The application maintains a chronological history of recent assessments, allowing users to review previous structural evaluations.

### 📄 Inspection Reports

Users can generate **print-ready inspection reports** containing assessment results and structural parameters for documentation and review.

### 🌙 Responsive Interface

* Responsive web interface
* Dark-mode focused design
* Interactive numeric controls
* Dynamic sliders
* SVG-based visualizations
* Lightweight frontend implementation

---

## 🧠 How It Works

The assessment follows a simple workflow:

```text
Structural Parameters
        ↓
User Input
        ↓
Risk Evaluation
        ↓
Failure Probability
        ↓
Risk Classification
        ↓
10-Year Forecast
        ↓
Inspection Report
```

Users provide structural and environmental information, after which StructureX processes the parameters and produces a risk assessment.

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript (ES6+)
* SVG Visualizations

### Deployment

* Vercel

### Machine Learning / Backend

The project can be extended with a Python-based machine learning backend using:

* Python
* Flask
* Scikit-learn
* Random Forest Classifier

---

## 🚀 Live Demo

Try StructureX here:

👉 **https://structurex-five.vercel.app/**

---

## 📊 Assessment Parameters

| Parameter            | Unit / Scale | Purpose                               |
| -------------------- | ------------ | ------------------------------------- |
| Age of Structure     | Years        | Represents structural aging           |
| Crack Width          | mm           | Indicates visible structural cracking |
| Vibration Level      | Hz           | Represents vibration characteristics  |
| Load Stress Capacity | %            | Represents load-related stress        |
| Weather Impact       | 1–10         | Represents environmental exposure     |
| Maintenance History  | 1–10         | Represents maintenance condition      |

---

## 🔮 Future Improvements

Potential future versions of StructureX could include:

* 🤖 Real-world ML model trained on structural inspection datasets
* 📡 IoT sensor integration for real-time monitoring
* 📷 Computer vision-based crack detection
* 🗺️ Geographic infrastructure risk mapping
* 📱 Mobile application
* 🔔 Automated maintenance alerts
* ☁️ Cloud-based inspection history
* 👥 Multi-user engineer dashboards
* 📑 Advanced engineering report generation
* 🔐 Authentication and role-based access

---

## ⚠️ Disclaimer

StructureX is a **prototype / decision-support application** and should not be used as a replacement for professional structural engineering inspection, analysis, or certification.

Actual structural safety assessments should be performed by qualified structural engineers using appropriate engineering standards, physical inspections, measurements, and validated analytical methods.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## 🌐 Project

**StructureX — AI Structural Health & Risk Predictor**

🔗 **Live Application:** https://structurex-five.vercel.app/

Built as an exploration of **AI, data-driven risk assessment, and structural health monitoring**.
