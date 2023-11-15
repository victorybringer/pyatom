# -*- coding: UTF-8 -*-
import logging
import os
import time
import colorlog


log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }

def gen_logger():
    logger = logging.getLogger('auto-itis')
  

    cfmt = '%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    colorformatter = colorlog.ColoredFormatter(cfmt, log_colors=log_colors)


    # StreamHandler to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(colorformatter)

 
    logger.addHandler(stream_handler)  
    logger.setLevel(logging.DEBUG)
    return logger

class Logger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self,):
      

        self.logger = gen_logger()

    def __getattr__(self, name):
        # if name not exist, trafer it to self.logger.name()
        def wrapper(*args, **kwargs):
            attr = getattr(self.logger, name)
            return attr(*args, **kwargs)
        return wrapper

log = Logger().logger
