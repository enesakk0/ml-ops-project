from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, inspect, Session
import os

load_dotenv("/home/train/mlops/week6_mlops/12_homework_fastapi_db_streamlit_mlflow/.env")

ROOT_DATABASE = os.getenv("MYSQL_DATABASE")
ROOT_USER = os.getenv("MYSQL_USER")
ROOT_PASSWORD = os.getenv("MYSQL_PASSWORD")

engine = create_engine(f"mysql+pymysql://{ROOT_USER}:{ROOT_PASSWORD}@localhost:3306/{ROOT_DATABASE}", echo=True)
inspector = inspect(engine)

def create_tables_sql():
    SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()