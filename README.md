# Coursera Project: Course Success Prediction Web App

This project is a **Course Success Prediction** application built using **Python, Flask, and a trained machine learning model**. The goal is to predict whether a student will successfully complete a course based on features such as participation, engagement, and prior performance. The project covers **data preprocessing, feature engineering, model training**, and **deployment via a web interface**.

## Project Details
- Historical course and student data is collected and cleaned.
- Features like **quiz scores, assignment submissions, forum activity, and login frequency** are used to assess engagement.
- A **Gradient Boosting classifier** is trained to predict course success (pass/fail).
- Users can input student data in the web app and get a **predicted outcome** for course completion.

## Features
- Web interface to input student/course details
- Predicts the likelihood of course success using a pre-trained ML model (`model.pkl`)
- Displays results dynamically on the web page
- All preprocessing and prediction logic is handled in the backend

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Coursera.git
