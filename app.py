from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class House(BaseModel):
    carpet_area: float

@app.get("/")
def home():
    return {
        "message": "Welcome to House Price Prediction API"
    }

@app.post("/predict")
def predict(data: House):

    prediction = model.predict([[data.carpet_area]])

    return {
        "predicted_price": float(prediction[0])
    }