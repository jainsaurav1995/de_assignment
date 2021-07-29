from boto3 import client
from config import EMAIL_ID, logger, ENV_TYPE


def send(message):
    logger.info('app.services.send_error_mail.send')
    mailer_client = client('ses')

    mailer_client.send_email(
        Destination={
            'ToAddresses': [
                EMAIL_ID
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Customer load failed in ' + ENV_TYPE + ' environment',
            },
        },
        Source=EMAIL_ID,
    )
