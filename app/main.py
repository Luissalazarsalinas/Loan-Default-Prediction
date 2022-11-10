import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, status

# App
app = FastAPI(
    version = "0.1.0",
    debug = True
)

# Model path
BASEPATH = Path(__file__).resolve(strict= True).parent

# load the model
with open(f"{BASEPATH}/LD_xgb_Model-0.0.1.pkl", "rb") as file:
    model = joblib.load(file)

# Home path 
@app.get("/home")
def home_path():
    return {
        "Message": "Machine learning API to detect loan default",
        "Api Health": "OK",
        "Api Version": "0.1.0"
        }

# Validation data
class FeaturesData(BaseModel):
    NAICS_2DIG: int
    Term: int
    NoEmp: int
    New: int
    DisbursementGross: float
    GrAppv: float
    SBA_Appv: float
    Recession: int
    RealEstate: int
    portion: float

# Prediciton path
@app.post("/inferece", status_code = status.HTTP_201_CREATED)
def prediction(data: FeaturesData):

    # dictionary
    data = data.dict()
    
    # dataframe
    features = pd.DataFrame(data, index = [0])

    # Predicitons
    pred = model.predict(features)
    pred_prob = model.predict_proba(features)
    # soft probabilities
    pred_full = np.round(pred_prob[0,0]*100, 2) 
    pred_default = np.round(pred_prob[0,1]*100, 2)

    if pred == 1:
        return {
            "status" : "Unapproved, potential loan default",
            "score" : pred_default
            }
    else:
        return {
            "status" : "Potentially approved",
            "score" : pred_full
        }
