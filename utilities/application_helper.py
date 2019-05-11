import time
from datetime import datetime

from utilities.logging_manager import initialise_logging

logger = initialise_logging(__file__, __name__)


# Record application start
def start_application():
    start_time = datetime.now()
    logger.info("Application started")
    time.sleep(1)
    return start_time


# Record application end and time elapsed
def end_application(start_time):
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    logger.info(f"Application ended (time elapsed: {time_elapsed})")
