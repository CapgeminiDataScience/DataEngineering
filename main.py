import sys
import os

from utilities.application_helper import start_application, end_application
from utilities.logging_manager import initialise_logging


def main():

    print(os.path.dirname(__file__))

    start = start_application()
    logger = initialise_logging(__file__, __name__)
    logger.info("Success")

    end_application(start)


if __name__ == "__main__":

    main()
