import os
import datetime
import time


ct = datetime.datetime.now()
str_ct = ct.strftime('%H:%M:%S')
print(str_ct) 
      
# h = str_ct[0]
# hh = str_ct[1]
# m = str_ct[3]
# mm = str_ct[4]
# s = str_ct[6]
# ss = str_ct[7]


# print(h, hh, m, mm, s, ss)
b = "\u2588"






td = datetime.timedelta(seconds=1)
s = ct + td    