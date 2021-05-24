import time
import datetime
# from datetime.timedelta import total_seconds
x = datetime.datetime.now()
time.sleep(5)
y = datetime.datetime.now()
time_delta = (y - x)
total_seconds = time_delta.total_seconds()

print(total_seconds)
