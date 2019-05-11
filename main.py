from utilities.application_helper import start_application, end_application
from utilities.logging_manager import initialise_logging


if __name__ == "__main__":

    start = start_application()
    logger = initialise_logging(__file__, __name__)

    file = open("/tmp/test.txt", "w+")
    file.write("Success")
    file.close()
    logger.info("Success")

    end_application(start)
