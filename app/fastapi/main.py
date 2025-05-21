from fastapi import FastAPI
from router import churn
from database import create_tables_sql
import os

create_tables_sql()

app = FastAPI()
app.include_router(churn.router)