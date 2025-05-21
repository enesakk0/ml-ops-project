from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from models import request_churn, churn
from database import get_db 
from sqlmodel import Session, select
import os
import pandas as pd
from mlflow.sklearn import load_model

router = APIRouter()

os.environ['MLFLOW_TRACKING_URI'] = 'http://localhost:5001/'
MODEL_NAME = "BankChurnModels"
MODEL_VERSION = 1

model = load_model(
    model_uri=f"models:/{MODEL_NAME}/{MODEL_VERSION}"
)

def make_prediction_churn(model, request):
    df = pd.DataFrame([request])
    prediction = model.predict(df)
    return int(prediction[0])

def insert_log_sql(request, prediction, client_ip, db):
    churn_list = churn(
            Age_censored=request["Age_censored"],
            EstimatedSalary=request["EstimatedSalary"],
            Balance=request["Balance"],
            Tenure=request["Tenure"],
            Geography=request["Geography"],
            Gender=request["Gender"],
            NumOfProducts=request["NumOfProducts"],
            IsActiveMember=request["IsActiveMember"],
            prediction=prediction,
            clientip=client_ip
    )

    with db as session:
        session.add(churn_list)
        session.commit()
        session.refresh(churn_list)

    return 1

@router.post("/churn/prediction")
async def post_churn_prediction(request: request_churn, fastapi_freq: Request, db: Session = Depends(get_db)):
    prediction = make_prediction_churn(model, request=request.dict())
    insert_log = insert_log_sql(request=request.dict(), prediction=prediction, client_ip=fastapi_freq.client.host, db=db)
    return {"prediction" : prediction}