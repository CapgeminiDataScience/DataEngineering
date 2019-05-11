
import logging
import os
import re
import sys
import traceback
from logging.config import fileConfig

from settings import PROJECT_DIRECTORY


def initialise_logging(filepath, name) -> logging.Logger:

    """
    Set up logging under the project directory and return a logger instance

    :param filepath:    Filepath of script calling method (__file__)
    :param name:        Python file for log formatting (__name__)
    :return:            Logger instance linked to directory containing file

    """

    # Get target directories
    directory = os.path.dirname(filepath)
    log_directory = f"{PROJECT_DIRECTORY}/log"

    try:
        # Standardise file paths to work with Windows & Linux systems
        directory = directory.replace("\\", "/")
        log_directory = log_directory.replace("\\", "/")

        # Set the log file name as the most nested directory
        search = re.search(r'.*/([\w\-_]+)', directory)
        filename = f"{log_directory}/{search.group(1)}.log"

    except AttributeError:
        print(traceback.format_exc())
        print("No suitable path found for log file")
        print(f"Full file path: {filepath}")
        print(f"Containing directory: {directory}")
        sys.exit()

    # Create log directory under project directory if not found
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Load logging configuration file
    fileConfig(f"{PROJECT_DIRECTORY}/logging.ini", disable_existing_loggers=False, defaults={"logname": filename})

    return logging.getLogger(name)
