# 📧 Spam Detection API

FastAPI + Scikit-Learn + Docker + Render

A production-ready email spam detection API powered by a trained
scikit-learn TF-IDF + Logistic Regression model.\
Deployed live on Render:

👉 **API Base URL:** https://email-spam-detector-vi0t.onrender.com\
👉 **Predict Endpoint:**
https://email-spam-detector-vi0t.onrender.com/predict

## 🚀 Features

-   Real-time spam classification\
-   FastAPI backend\
-   Pre-trained ML pipeline (`spam_pipeline.pkl`)\
-   Dockerized for consistent deployment\
-   Fully deployed on Render

## 📁 Project Structure

email-spam-detection/ │── ml_api.py │── requirements.txt │── Dockerfile
│── README.md │── .gitignore └── model/ └── spam_pipeline.pkl

## ✅ How to Use the API

### POST /predict

URL: https://email-spam-detector-vi0t.onrender.com/predict

Request Body: { "message": "Congratulations! You've won a free prize!" }

Response: { "spam": true }

## 🧪 Local Development Setup

python3 -m venv venv source venv/bin/activate

pip install -r requirements.txt

uvicorn ml_api:app --reload

Local server: http://127.0.0.1:8000

## 🐳 Run with Docker

docker build -t spam-api . docker run -p 10000:10000 spam-api

## ☁️ Deploying on Render

1.  Push to GitHub\
2.  Render → New Web Service\
3.  Choose Docker\
4.  Render builds & deploys automatically

## ⚠️ Troubleshooting

FileNotFoundError: spam_pipeline.pkl → commit the model file.
