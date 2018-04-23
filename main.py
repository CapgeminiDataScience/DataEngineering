
from common.application_helper import start_application, end_application

start = start_application()

file = open("/tmp/test.txt", "w+")
file.write("Success")
file.close()

end_application(start)
