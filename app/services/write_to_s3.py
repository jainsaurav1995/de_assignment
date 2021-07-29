from io import StringIO
import boto3
from datetime import timedelta, date
from config import logger, UPLOAD_BUCKET_NAME, FILE_NAME


def upload(data_frame):
    logger.info('app.services.write_to_s3.upload')
    bucket = UPLOAD_BUCKET_NAME
    csv_buffer = StringIO()
    data_frame.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    yesterday = date.today() - timedelta(days=1)
    s3_resource.Object(bucket, str(yesterday.year) + '/' + str(yesterday.month) + '/' +
                       str(yesterday.day) + '/' + FILE_NAME).put(Body=csv_buffer.getvalue())
