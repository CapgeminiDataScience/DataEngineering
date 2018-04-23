import logging
import os


# Important directories
HOME_DIRECTORY = os.getenv('HOME')
PROJECT_DIRECTORY = os.getcwd()

# Logging setup
default_formatter = logging.Formatter("%(asctime)-15s %(levelname)-5s %(name)-25s - %(message)s")
console_handler = logging.StreamHandler()
root = logging.getLogger()
console_handler.setFormatter(default_formatter)
root.addHandler(console_handler)
root.setLevel(logging.DEBUG)
