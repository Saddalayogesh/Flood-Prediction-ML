# 🌊 Rising Waters: A Machine Learning Approach to Flood Prediction

<p align="center">
  <b>Flood Prediction using Machine Learning & Flask Web Application</b><br>
  <i>Real-time disaster prediction system using meteorological data</i>
</p>

---

## 📌 Overview

Flood Prediction using Machine Learning is a web-based application designed to forecast the possibility of flood occurrence based on meteorological parameters.

The system analyzes historical weather data using supervised Machine Learning algorithms and provides real-time predictions through a **Flask-based web interface**.

This project demonstrates the practical application of Machine Learning in **disaster management and early warning systems**.

---

## 👥 Team Details

* **Team ID:** LTVIP2026TMIDS38167
* **Team Size:** 4

### 👑 Team Leader

* Saddala Yogesh

### 👨‍💻 Team Members

* Bolligarla Nikhitha
* C L Indira
* C Harsha Vardhan Reddy

---

## ⚠️ Problem Statement

Floods are among the most devastating natural disasters, causing severe damage to infrastructure, agriculture, and human life.

Traditional forecasting methods often fail to capture complex relationships between meteorological variables.

This project aims to build an intelligent system using Machine Learning to accurately predict flood occurrence.

---

## 🎯 Project Objectives

* Collect and analyze historical meteorological data
* Perform data preprocessing and cleaning
* Implement multiple ML classification algorithms
* Evaluate models using performance metrics
* Select the best-performing model
* Deploy using Flask
* Provide real-time prediction through a web interface

---

## 📊 Dataset Description

The dataset includes the following features:

* Temperature
* Humidity
* Cloud Cover
* Annual Rainfall
* Jan–Feb Rainfall
* Mar–May Rainfall
* Jun–Sep Rainfall
* Oct–Dec Rainfall
* Average June Rainfall
* Subdivision Code

### 🎯 Target Variable

* **1 → Flood Occurred**
* **0 → No Flood**

---

## 🛠️ Tech Stack

* **Programming:** Python 3.10
* **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, XGBoost, Joblib
* **Framework:** Flask
* **Frontend:** HTML, CSS, Bootstrap
* **Tools:** PyCharm
* **Version Control:** Git & GitHub

---

## 🧠 Machine Learning Models

* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* XGBoost Classifier

✅ **Final Model Selected:** XGBoost (Best performance)

---

## 📈 Model Evaluation Metrics

* Accuracy Score
* Confusion Matrix
* Precision
* Recall
* F1-Score

---

## 🏗️ System Architecture

User Input (HTML Form)
→ Flask Backend (app.py)
→ Feature Scaling (StandardScaler)
→ Trained XGBoost Model
→ Prediction Output (Web Interface)

---

## 📁 Project Structure

```id="z7x8la"
Flood-Prediction-ML/
│── app.py
│── floods.save
│── transform.save
│── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── nochance.html
```

---

## ▶️ How to Run

```bash id="wq7d1c"
# Clone repository
git clone https://github.com/YOUR-USERNAME/Flood-Prediction-ML.git

# Navigate to folder
cd Flood-Prediction-ML

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

---

## 🌐 Access the App

Open in browser:

```
http://127.0.0.1:5000
```

---

## ✨ Features

* Real-time flood prediction
* ML model integration
* Responsive web interface
* Scalable system architecture
* High prediction accuracy

---

## ✅ Advantages

* Supports early warning systems
* Helps disaster management planning
* Real-world ML application
* Modular and extendable design

---

## 🚀 Future Enhancements

* Integration with real-time weather APIs
* Cloud deployment (AWS / Render)
* SMS & Email alerts
* Mobile application development
* Deep learning model integration

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be effectively applied to predict floods using meteorological data.

The use of **XGBoost** ensures high accuracy, while **Flask** enables real-time deployment through a user-friendly interface.

This system can be extended into a full-scale disaster management solution.

---

## 📅 Year

2026

---

## 🔗 License

This project is developed for educational and academic purposes.
