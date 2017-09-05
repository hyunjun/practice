import logging
import logging.config
import logging.handlers
import os
import yaml


def setup_logging(default_path='common/config/logging.yaml'):
  path = default_path
  if os.path.exists(path):
    with open(path, 'rt') as f:
      config = yaml.safe_load(f.read())
      logging.config.dictConfig(config)
  else:
    logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
  setup_logging(os.environ.get('LOGGING_CONFIG_FILEPATH'))
  logger1 = logging.getLogger('test_both')
  logger1.debug('logging test 1')
  logger2 = logging.getLogger('test_file')
  logger2.debug('logging test 2')
  logger3 = logging.getLogger('test_null')
  logger3.debug('logging test 3')

  # https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
  # https://docs.python.org/3/howto/logging-cookbook.html#using-file-rotation
  logger = logging.getLogger('TEST')
  # https://stackoverflow.com/questions/2266646/how-to-i-disable-and-re-enable-console-logging-in-python
  #logger.propagate = False
  FORMAT = "%(asctime)s [%(levelname)s][%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
  logger.setLevel(logging.DEBUG)
  #ch = logging.StreamHandler(sys.stdout)
  ch = logging.handlers.TimedRotatingFileHandler('logs/timed.log', when="midnight", interval=1, backupCount=100)
  ch.setFormatter(logging.Formatter(FORMAT))
  logger.addHandler(ch)
  for i in range(10):
    logger.debug('timed test {}'.format(i))
