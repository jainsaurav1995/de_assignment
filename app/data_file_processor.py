from config import logger
from app.services.download_file import download
from app.services.parse_raw_data import parse
from app.services.write_to_s3 import upload
from app.services.split_data_frames import split
from app.services.write_to_db import write
from app.services.send_error_mail import send
from app.validations.data_validations import validate


def process():
    try:
        download()
        data_frame = parse()
        validate(data_frame)
        upload(data_frame)
        country_data = split(data_frame)
        write(country_data)
    except Exception as ex:
        logger.exception('Internal server error')
        send('ERROR - \n' + str(ex))
