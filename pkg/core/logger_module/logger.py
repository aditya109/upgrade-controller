import logging


def get_configured_logger(application_name):
    """
    Returns a logger object which is confured to stream handle and file handle according to set format
    :param application_name:string
    :return: Logger
    """

    logger = logging.getLogger(f"{application_name}-logs")

    # configuration of handlers for logger objects
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"C:\\{application_name}\\logs\\{application_name}_log", "w")

    # creating formatter
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    # setting formatter for logger objects
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # adding handlers for logger objects
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
