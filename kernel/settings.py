import tomllib
import logging.config
from pathlib import Path

from painless.utils.funcs import DirectoryCreator

BASE_DIR = Path(__file__).resolve().parent.parent

with open('settings.toml', 'rb') as sf:
    config = tomllib.load(sf)

DIRECTORIES = config['log']['LOG_DIRS']

DirectoryCreator(BASE_DIR, DIRECTORIES)

with open('config/logging.toml', mode='rb') as config_file:
    log_conf_dict = tomllib.load(config_file)
    logging.config.dictConfig(log_conf_dict)
