# ☄️ Asteroid Hazard Prediction System

A Machine Learning web application that predicts whether a Near-Earth Asteroid (NEA) is hazardous based on its physical and orbital characteristics.

## 🚀 Live Demo

https://asteroid-hazard-prediction-veunrokxjpsrwlajmqzheu.streamlit.app/

## 📌 Project Overview

This project uses machine learning to classify asteroids as **Hazardous** or **Non-Hazardous** based on astronomical observations obtained from NASA Near-Earth Object datasets.

The system performs data preprocessing, feature engineering, model training, evaluation, and deployment through a Streamlit web application.

## 📊 Dataset Information

* Source: NASA Near-Earth Object Dataset
* Records: 90,836 asteroids
* Target Variable: `hazardous`
* Class Distribution:

  * Non-Hazardous: ~90.3%
  * Hazardous: ~9.7%

## 🔧 Feature Engineering

Original Features:

* Estimated Diameter Minimum
* Estimated Diameter Maximum
* Relative Velocity
* Miss Distance
* Absolute Magnitude

Engineered Feature:

* Average Diameter

Feature Formula:

avg_diameter = (est_diameter_min + est_diameter_max) / 2

Final Features Used:

* Relative Velocity
* Miss Distance
* Absolute Magnitude
* Average Diameter

## 🤖 Machine Learning Pipeline

### Data Preprocessing

* Removed irrelevant columns
* Converted target labels
* Created engineered features
* Train-Test Split (80:20)
* Stratified Sampling

### Class Imbalance Handling

The dataset was highly imbalanced.

Techniques explored:

* Baseline Random Forest
* Random Forest with Class Weights
* SMOTE Oversampling

### Algorithms Evaluated

1. Random Forest Classifier
2. Random Forest + Class Weights
3. Random Forest + SMOTE

## 📈 Model Evaluation

Metrics Used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Final Model Performance

Accuracy: 92%

Hazardous Class:

* Precision: 0.62
* Recall: 0.36
* F1 Score: 0.46

Confusion Matrix:

[[16011   389]
[ 1123   645]]

## 🎯 Feature Importance

| Feature            | Importance |
| ------------------ | ---------- |
| Absolute Magnitude | 38.6%      |
| Average Diameter   | 30.1%      |
| Relative Velocity  | 16.8%      |
| Miss Distance      | 14.6%      |

Key Insight:

Absolute Magnitude and Average Diameter were the most influential predictors for determining asteroid hazard status.

## 🌐 Deployment

* Frontend: Streamlit
* Model Serialization: Joblib
* Version Control: Git & GitHub
* Cloud Deployment: Streamlit Community Cloud

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Imbalanced-Learn (SMOTE)
* Streamlit
* Joblib

## ▶️ Run Locally

git clone https://github.com/Sanjeev-Karnatapu/asteroid-hazard-prediction.git

cd asteroid-hazard-prediction

pip install -r requirements.txt

streamlit run app/streamlit_app.py
