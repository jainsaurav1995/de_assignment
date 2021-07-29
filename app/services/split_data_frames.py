from config import logger


def split(data_frame):
    logger.info('app.services.split_data_frames.split')
    countries = data_frame.groupby('Country').groups.keys()
    country_data = {}
    for country in countries:
        country_data[country] = data_frame[data_frame.Country == country]
        country_data[country].drop('Country', axis=1, inplace=True)
    return country_data
