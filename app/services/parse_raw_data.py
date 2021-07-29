import pandas
from config import logger, FILE_NAME, DATA_TYPES, DATE_COLUMNS


def parse():
    logger.info('app.services.parse_raw_data.parse')
    df = pandas.read_csv(FILE_NAME, delimiter='|', header=0, dtype=DATA_TYPES)
    df.drop([df.columns[0], df.columns[1]], axis=1, inplace=True)
    for column, date_format in DATE_COLUMNS.items():
        df[column] = pandas.to_datetime(df[column], format=date_format)
    return df
