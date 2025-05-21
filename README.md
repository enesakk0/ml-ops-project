# 🧠 Churn Prediction ML Model and API Deployment

This project focuses on developing a machine learning (ML) model designed to predict customer churn risk. The core objective is to empower businesses with data-driven decision-making capabilities that foster longer-lasting relationships with their existing customers.

The project encompasses the following key stages:

* **Data Preprocessing**: Raw data was meticulously cleaned, missing values were handled, and the dataset was prepared for model training.
* **Feature Engineering**: Meaningful features reflecting customer behavior and trends were created to enhance model performance.
* **Machine Learning Model Selection**: Various algorithms were explored and evaluated to classify churn, and the top-performing model was selected.
* **Model Evaluation**: The model's success was rigorously assessed using key metrics such as accuracy, F1-score, and ROC-AUC.
* **API Integration**: The trained model was encapsulated within a Flask-based REST API, transforming it into a real-time prediction service accessible by external systems.
* **Logging & Database Integration**: Specifically on the API side, request details, user information, and prediction results are automatically logged and stored in an SQL database table.
* **Docker Deployment**: The entire project was containerized using Docker, making it easy to deploy and ensuring consistency across different environments.

This project delivers an end-to-end machine learning pipeline, covering both technical implementation and business utility. By creating a system suitable for real-world application, it offers a robust solution infrastructure for companies aiming to boost customer loyalty.

## **Setup Instructions**

#### **Creating the `requirements.txt` file for library dependencies**
```
cat <<EOF>> requirements.txt
fastapi[all]==0.115.5
uvicorn[standard]==0.32.0
sqlmodel==0.0.22
pandas== 2.2.3
scikit-learn==1.5.2
mlflow==2.17.2
joblib==1.4.2
pymysql==1.1.1
python-dotenv==1.0.1
streamlit
matplotlib
seaborn
jupyterlab
feature_engine
xgboost
EOF
```

### Initiating Docker Environments
```commandline
docker-compose up -d
```

### Creating a New Conda Environment
```commandline
conda create --name mlops
conda activate mlops
```

### Installing Python Libraries
```
python -m pip install -r requirements.txt
```

### ML Development and Creation Phases

#### Launching the Jupyter Environment
```python
jupyter lab
```

#### Model Development Stages
```commandline
train/001_ml_prediction_dataset_analysis.ipynb
```