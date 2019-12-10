#!/usr/bin/env python
import logging
from configs.webhook_configs import logging_dir, logging_level

''' Create and configure logger object '''
logger = logging.getLogger()
level = logging.getLevelName(logging_level)
logger.setLevel(level)

''' Format logging message '''
format_str = '%(asctime)s (%(levelname)s) - %(message)s'
logging.basicConfig(filename=logging_dir, format=format_str, filemode='a')