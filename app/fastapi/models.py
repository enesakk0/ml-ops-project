from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class churn(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Age_censored: int
    EstimatedSalary: float
    Balance: float
    Tenure: int
    Geography: str
    Gender: str
    NumOfProducts: int
    IsActiveMember: int
    prediction: float
    predictiontime: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    clientip: str

class request_churn(BaseModel):
    Age_censored: int
    EstimatedSalary: float
    Balance: float
    Tenure: int
    Geography: str
    Gender: str
    NumOfProducts: int
    IsActiveMember: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "Age_censored": 42,
                "EstimatedSalary": 2498,
                "Balance": 6743,
                "Tenure": 5,
                "Geography": "Germany",
                "Gender": "Male",
                "NumOfProducts": 2,
                "IsActiveMember": 1
            }
        }