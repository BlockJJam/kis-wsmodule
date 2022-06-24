import logging

def _formatter():
    return logging.Formatter("\033[0;34m[%(asctime)s - %(name)s - %(levelname)s]\033[0m %(message)s")

def _stream_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(_formatter())
    return handler

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(_stream_handler())
    logger.propagate = 0
    return logger


logger = get_logger()

'''
쓰는 형테: logger.error(f'[CONTROLLER] {e}')
'''
