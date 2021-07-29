from boto3 import client
from datetime import timedelta, date
from config import logger, DOWNLOAD_BUCKET_NAME, FILE_NAME


def download():
    logger.info('app.services.download_file.download')
    s3 = client('s3')
    yesterday = date.today() - timedelta(days=1)
    s3.download_file(DOWNLOAD_BUCKET_NAME, str(yesterday.year) + '/' + str(yesterday.month) + '/' +
                     str(yesterday.day) + '/' + FILE_NAME, FILE_NAME)
