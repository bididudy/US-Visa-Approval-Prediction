import os
from datetime import date

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

MANGODB_URL_KEY = "MANGODB_URL"

PIPELINE_NAME = "usvisa"

ARTIFACT_DIR = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

'''
Data ingestion related constants start with DATA INGESTION VAR NAME
'''
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DATA: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
