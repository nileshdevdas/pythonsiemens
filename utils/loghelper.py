import logging as logger;
logger.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='c:/myapp.log',
        level=logger.DEBUG)

def getLogger():
    return logger;
