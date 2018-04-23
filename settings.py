import logging
import os


# Important directories
HOME_DIRECTORY = os.getenv('HOME')
PROJECT_DIRECTORY = os.getcwd()

# Create parent logger
root = logging.getLogger()

# Define logging format
default_formatter = logging.Formatter("%(asctime)-15s %(levelname)-5s %(name)-25s - %(message)s")

# Setup logging handler with file output
file_handler = logging.FileHandler("logs/template-project-python.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(default_formatter)

# Setup logging handler with console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(default_formatter)

# Add logging handlers
root.addHandler(file_handler)
root.addHandler(console_handler)
root.setLevel(logging.DEBUG)
