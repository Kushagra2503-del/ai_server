from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class PlayerStats(BaseModel):
    level: int
    hours: int

@app.post("/predict")
def predict_match(player: PlayerStats):
    features = np.array([[player.level, player.hours]])
    prediction = model.predict(features)[0]
    return {"ai_prediction": "Victory" if prediction == 1 else "Defeat "}