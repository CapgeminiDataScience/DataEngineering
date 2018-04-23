
import logging

import settings
from common.application_helper import start_application, end_application

log = logging.getLogger('main')

start = start_application()

file = open("/tmp/test.txt", "w+")
file.write("Success")
file.close()
log.info("Success")

end_application(start)
