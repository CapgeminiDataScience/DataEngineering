import logging
import time
from datetime import datetime


log = logging.getLogger(__name__)


# Record application start
def start_application():
    start_time = datetime.now()
    log.info("Application started")
    time.sleep(1)
    return start_time


# Record application end and time elapsed
def end_application(start_time):
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    log.info("Application ended")
    log.info(f"Time elapsed: {time_elapsed}")
