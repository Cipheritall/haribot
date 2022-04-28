import logging
from config import *
from datetime import datetime

def get_debug_level():
    configuration = get_setup_config()
    if configuration['loggin_setup']['log_folder'] == "debug":
        return logging.DEBUG
    elif configuration['loggin_setup']['log_folder'] == "info":
        return logging.INFO
    elif configuration['loggin_setup']['log_folder'] == "warning":
        return logging.WARNING
    elif configuration['loggin_setup']['log_folder'] == "error":
        return logging.ERROR
    elif configuration['loggin_setup']['log_folder'] == "critical":
        return logging.CRITICAL
    return logging.DEBUG

def init_logging():
    configuration = get_setup_config()
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y.%H_%M_%S")
    file_name = configuration['loggin_setup']['log_folder']+"/log"+dt_string+".log"
    logging.basicConfig(filename=file_name, filemode='w', format=configuration['loggin_setup']['format'], level=get_debug_level())
    logging.warning('This will get logged to a file')
    return logging