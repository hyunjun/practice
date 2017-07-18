import logging.config
import os
import sys
import yaml


sys.path.append(os.path.join(os.path.abspath('.'), '..', '..'))


def setup_logging(default_path='common/config/logging.yaml'):
  path = default_path
  if os.path.exists(path):
    with open(path, 'rt') as f:
      config = yaml.safe_load(f.read())
      logging.config.dictConfig(config)
  else:
    logging.basicConfig(level=default_level)
