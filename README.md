# Asteroid Hazard Prediction System

## Overview

This project uses Machine Learning to predict whether a Near-Earth Asteroid is hazardous using NASA asteroid observation data.

## Dataset

NASA Near Earth Objects (NEO) Dataset from Kaggle.

* 90,836 asteroid observations
* Binary classification problem (Hazardous / Non-Hazardous)

## Features Used

* Relative Velocity
* Miss Distance
* Absolute Magnitude
* Average Diameter

## Models Evaluated

* Logistic Regression
* Weighted Logistic Regression
* Random Forest
* Tuned Random Forest

## Best Model

Tuned Random Forest

Performance:

* Accuracy: 80%
* Hazardous Recall: 98%

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Run Locally

```bash
pip install -r requirements.txt

streamlit run app/streamlit_app.py
```
