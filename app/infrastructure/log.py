import os
from configparser import ConfigParser
from logging.config import fileConfig


def configure_logging() -> None:
    config = ConfigParser(os.environ)
    config.read(filenames="app/infrastructure/logging.ini")
    fileConfig(config)
