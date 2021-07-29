from sqlalchemy import create_engine
from config import logger, DB_ENDPOINT, DB_NAME, DB_USER, DB_PASSWORD


def write(country_data):
    logger.info('app.services.write_to_db.write')
    alchemy_engine = create_engine(
        'postgresql+psycopg2://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_ENDPOINT + ':5432' +
        '/' + DB_NAME)
    connection = alchemy_engine.connect()
    for country, data_frame in country_data.items():
        data_frame.to_sql('table_' + country, connection, if_exists='append')
