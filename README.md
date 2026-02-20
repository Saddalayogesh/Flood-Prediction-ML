Rising Waters: A Machine Learning Approach to Flood Prediction

Flood Prediction using Machine Learning is a web-based application designed to forecast the possibility of flood occurrence based on meteorological parameters. The system analyzes historical weather data using supervised Machine Learning algorithms and provides real-time predictions through a Flask-based web interface.

This project demonstrates the practical application of Machine Learning in disaster management and early warning systems.

Team Details

Team ID: LTVIP2026TMIDS38167

Team Size: 4

Team Leader   :   Saddala Yogesh

Team Members:

Bolligarla Nikhitha

C L Indira

C Harsha Vardhan Reddy

Problem Statement

Floods are among the most devastating natural disasters, causing severe damage to infrastructure, agriculture, and human life. Traditional flood forecasting methods often rely on statistical models that may not accurately capture complex relationships between meteorological variables.

The goal of this project is to build an intelligent flood prediction system using Machine Learning algorithms that can analyze historical weather data and classify whether there is a high possibility of flood occurrence.

Project Objectives

To collect and analyze historical meteorological data.

To preprocess and clean the dataset.

To implement multiple Machine Learning classification algorithms.

To evaluate models using performance metrics.

To select the best-performing model.

To deploy the trained model using Flask.

To provide real-time flood prediction through a user-friendly web interface.

Dataset Description

The dataset used for this project contains historical meteorological parameters including:

Temperature

Humidity

Cloud Cover

Annual Rainfall

Jan–Feb Rainfall

Mar–May Rainfall

Jun–Sep Rainfall

Oct–Dec Rainfall

Average June Rainfall

Subdivision Code

Flood (Target Variable)

Target Variable:

1 → Flood Occurred

0 → No Flood

The dataset was used for supervised classification to train and evaluate different Machine Learning models.

Technologies Used

Programming Language:

Python 3.10

Libraries:

NumPy

Pandas

Scikit-learn

Matplotlib

Seaborn

XGBoost

Joblib

Web Framework:

Flask

Frontend:

HTML

CSS

Bootstrap

Version Control:

Git & GitHub

Machine Learning Models Implemented

The following classification algorithms were implemented and compared:

Decision Tree Classifier

Random Forest Classifier

K-Nearest Neighbors (KNN)

XGBoost Classifier

After performance evaluation using accuracy score and confusion matrix, XGBoost was selected as the final model for deployment due to its consistent and reliable performance.

Model Evaluation Metrics

The models were evaluated using:

Accuracy Score

Confusion Matrix

Precision

Recall

F1-Score

The selected XGBoost model achieved high classification accuracy and minimal misclassification errors.

System Architecture

The system follows a layered architecture:

User Input (HTML Form)
→ Flask Backend (app.py)
→ Feature Scaling (StandardScaler)
→ Trained XGBoost Model
→ Prediction Output (Web Interface)

The trained model is saved as floods.save and the scaler object is saved as transform.save to avoid retraining during deployment.

Project Structure
Flood-Prediction-ML

│
├── app.py

├── floods.save

├── transform.save

├── requirements.txt

│

├── templates

│   ├── home.html

│   ├── index.html

│   ├── chance.html


│   └── nochance.html
How to Run the Project Locally

Step 1: Clone the repository

git clone https://github.com/YOUR-USERNAME/Flood-Prediction-ML.git

Step 2: Navigate to project folder

cd Flood-Prediction-ML

Step 3: Install required libraries

pip install -r requirements.txt

Step 4: Run the Flask application

python app.py

Step 5: Open in browser

http://127.0.0.1:5000
Features

Real-time flood risk prediction

Machine Learning model integration

Clean and responsive web interface

Scalable architecture

High prediction accuracy

Advantages

Supports early warning systems

Helps disaster response planning

Practical application of Machine Learning

Modular and extendable design

Future Enhancements

Integration with real-time weather APIs

Cloud deployment (Render / AWS)

SMS and email alert system

Mobile application development

Implementation of Deep Learning models

Conclusion

This project successfully demonstrates the integration of Machine Learning and web development for flood prediction. By analyzing meteorological parameters and applying supervised classification algorithms, the system provides accurate and real-time flood risk assessment.

The use of XGBoost ensures reliable performance, while Flask enables deployment through a user-friendly web interface. This solution can be extended further for real-world disaster management systems.
