import os
import datetime
import time

# ct = datetime.datetime.now()
# str_ct = ct.strftime('%H:%M:%S')
# td = datetime.timedelta(seconds=1)
# s = ct + td

while True:
    ct = datetime.datetime.now()
    str_ct = ct.strftime('%H:%M:%S')
    print(str_ct) 
    time.sleep(1)   
    os.system('cls' if os.name == 'nt' else 'clear')

