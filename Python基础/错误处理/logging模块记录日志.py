import logging
logging.basicConfig(filename=r'D:\Python\Log.log',filemode='a',level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',format="%(asctime)s %(filename)s"
                    "[line:%(lineno)d]%(levelname)s%(message)s")
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')