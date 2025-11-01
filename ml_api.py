from fastapi import FastAPI
from pydantic import BaseModel
import json
import pickle

app = FastAPI()

class model_input(BaseModel):
    message: str
    
# Load the pre-trained model
pipeline = pickle.load(open("./model/spam_pipeline.pkl", "rb"))


@app.post("/predict")
def predict_spam(payload: model_input):
    text = payload.message
    prediction = pipeline.predict([text])[0]
    is_spam = (prediction == 0)
    return {"spam": bool(is_spam)}  # Assuming 0 indicates spam
