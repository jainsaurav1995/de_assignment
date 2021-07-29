from config import logger, ESSENTIAL_COLUMNS, PRIMARY_KEY, DEDUPLICATION_KEY


def validate(data_frame):
    logger.info('app.validations.data_validations.validate')
    data_frame.dropna(subset=ESSENTIAL_COLUMNS, how='any', inplace=True)
    data_frame.sort_values(DEDUPLICATION_KEY).drop_duplicates(subset=PRIMARY_KEY, keep='last', inplace=True)
