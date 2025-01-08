import logging

def setup_logger(name, log_file='serve.log', level=logging.DEBUG):
    # Create a custom logger
    # logger = logging.getLogger('db_helper')
    logger = logging.getLogger(name)

    # Configure the custom logger
    # logger.setLevel(logging.DEBUG)
    logger.setLevel(level)
    # file_handler = logging.FileHandler('server.log')
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger