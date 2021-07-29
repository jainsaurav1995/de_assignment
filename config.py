from os import getenv
import logging
from datetime import date


logger = None

DB_ENDPOINT = getenv('DB_ENDPOINT', 'localhost:5432')
DB_NAME = getenv('DB_NAME', 'postgres')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DOWNLOAD_BUCKET_NAME = getenv('DOWNLOAD_BUCKET_NAME')
UPLOAD_BUCKET_NAME = getenv('UPLOAD_BUCKET_NAME')
FILE_NAME = getenv('FILE_NAME')
EMAIL_ID = getenv('EMAIL_ID')
ENV_TYPE = getenv('ENV_TYPE')
DATA_TYPES = {
    'Customer Name': str,
    'Customer ID': str,
    'Open Date': int,
    'Last Consulted Date': int,
    'Vaccination Type': str,
    'Doctor Consulted': str,
    'State': str,
    'Country': str,
    'Post Code': int,
    'DOB': int,
    'Active Customer': str
}
DATE_COLUMNS = {'Open_Date': '%Y%m%d', 'Last_Consulted_Date': '%Y%m%d', 'DOB': '%d%m%Y'}
ESSENTIAL_COLUMNS = ['Customer_Name', 'Customer_Id', 'Open_Date']
PRIMARY_KEY = 'Customer_Id'
DEDUPLICATION_KEY = 'Open_Date'


def get_logger():
    logging.basicConfig(level=getenv('LogLevel').upper(), format='%(filename)s:%(funcName)s - %(message)s')
    return logging.getLogger()


def set_configurations():
    global logger
    logger = get_logger()


set_configurations()
