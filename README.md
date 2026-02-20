🏥 Care Corner – Health Diagnosis & Recommendation System
📌 Project Overview

Care Corner is an AI-based healthcare support system developed using Machine Learning and Flask.
The system predicts diseases based on user-selected symptoms and provides:

🧠 Disease Prediction using Random Forest

🌿 Home Remedies Suggestions

🏥 Hospital Recommendations (Mysore region)

All recommendations are generated using structured CSV datasets.

🚀 Core Modules

1️⃣ Symptom Analyzer (Machine Learning Model)

🔹 Description

Users select symptoms from a predefined list in the web interface.
The system processes the input and predicts the most probable disease.

🔹 Model Used

Algorithm: Random Forest Classifier

Type: Multi-class Classification

Library: Scikit-learn

Dataset: CSV-based symptom-disease dataset

🔹 Working Process

Symptoms selected via HTML form

Input converted into numerical feature vector

Random Forest model predicts disease

Predicted disease displayed on result page

🔹 Why Random Forest?

High accuracy

Handles multiple features effectively

Reduces overfitting

Works well for medical classification problems

2️⃣ Home Remedies Recommendation

🔹 Description

Once disease is predicted, the system:

Searches disease name in remedies CSV file

Fetches corresponding home remedies

Displays user-friendly suggestions

🔹 Dataset Used

home_remedies.csv
Contains:

Disease name

Recommended home remedies

Basic precaution tips

🔹 Purpose

Helps users manage mild symptoms

Provides immediate first-level assistance

Educational healthcare support

3️⃣ Hospital Recommendation System (Mysore Based)

🔹 Description

The system recommends hospitals located in Mysore based on disease type.

🔹 Dataset Used

mysore_hospitals.csv
Contains:

Hospital name

Location

Specialization

Contact details

🔹 Working Logic

Match predicted disease with hospital specialization

Filter hospitals located in Mysore

Display relevant hospitals to user

🛠 Technologies Used

Python

Flask

Scikit-learn

Random Forest Classifier

Pandas & NumPy

CSV Dataset

HTML, CSS (Frontend)

VS Code

📊 Machine Learning Workflow

Load CSV dataset

Preprocess symptom features

Encode categorical labels

Train Random Forest model

Save trained model

Load model in Flask app

Predict disease based on user input

🎯 Project Objective

To create a simple AI-driven healthcare assistant that:

Helps users identify possible diseases early

Provides safe home remedies

Guides users to hospitals in Mysore

Demonstrates practical ML implementation

📈 Business / Real-World Use Case

Rural health assistance

Educational healthcare demo system

Mini telemedicine support tool

Academic Machine Learning project
