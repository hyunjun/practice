import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

logging.basicConfig(level=logging.DEBUG, format='   %(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')
logger = logging.getLogger()

#@profile   #   annotation for memory_profiler
def my_func():
    for i in range( 100000000 ):
        logger.debug( "TEST" )

if __name__ == '__main__':
    my_func()
