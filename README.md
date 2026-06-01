# ☄️ Asteroid Hazard Prediction System

## Overview

This project uses Machine Learning to predict whether a Near-Earth Asteroid is hazardous using NASA asteroid observation data.

The system performs data preprocessing, exploratory data analysis, feature engineering, model training, hyperparameter tuning, and deployment through an interactive Streamlit web application.

---

## Dataset

NASA Near Earth Objects (NEO) Dataset

* 90,836 asteroid observations
* Binary classification:

  * Hazardous
  * Non-Hazardous

---

## Features Used

* Relative Velocity
* Miss Distance
* Absolute Magnitude
* Average Diameter

---

## Machine Learning Pipeline

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Engineering
4. Handling Class Imbalance
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Streamlit Deployment

---

## Models Evaluated

| Model                        | Accuracy | Hazard Recall |
| ---------------------------- | -------- | ------------- |
| Logistic Regression          | 90%      | 8%            |
| Weighted Logistic Regression | 79%      | 93%           |
| Random Forest                | 92%      | 36%           |
| Tuned Random Forest          | 80%      | 98%           |

---

## Best Model

### Tuned Random Forest

Performance:

* Accuracy: 80%
* Hazardous Recall: 98%
* Only 28 hazardous asteroids missed during testing

---

## Application Screenshots

### Home Screen

![Home Screen](images/home.png)

### Safe Asteroid Prediction

![Safe Prediction](images/safe_prediction.png)

### Hazardous Asteroid Prediction

![Hazardous Prediction](images/hazardous_prediction.png)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib
* Matplotlib

---

## Project Structure

```text
asteroid_hazard_prediction/

├── app/
├── data/
├── images/
├── models/
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Run Locally

```bash
pip install -r requirements.txt

streamlit run app/streamlit_app.py
```
