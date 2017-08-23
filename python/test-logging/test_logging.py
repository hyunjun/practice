import logging
import logging.config
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
