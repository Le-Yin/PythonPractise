import time
import calendar

seconds = time.time()
print(seconds)

asctime = time.asctime(time.localtime(time.time()))
print(asctime) #Sun Mar 18 15:21:47 2018

calendar = calendar.month(2018, 3)
print(calendar)
