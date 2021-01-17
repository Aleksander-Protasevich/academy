import os
import datetime
import time
from digit import zero1, zero2, zero3, zero4, zero5, one1, one2, one3, one4, one5, two1, two2, two3, two4, two5, three1, three2, three3, three4, three5
from digit import four1, four2, four3, four4, four5, five1, five2, five3, five4, five5, six1, six2, six3, six4, six5
from digit import seven1, seven2, seven3, seven4, seven5, eight1, eight2, eight3, eight4, eight5, nine1, nine2, nine3, nine4, nine5

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    ct = datetime.datetime.now()
    str_ct1 = ct.strftime('%H  %M  %S')
    str_ct2 = ct.strftime('%H  %M  %S')
    str_ct3 = ct.strftime('%H  %M  %S')
    str_ct4 = ct.strftime('%H  %M  %S')
    str_ct5 = ct.strftime('%H  %M  %S')
    
    line1 = {'0' : zero1, '1': one1, '2' : two1, '3' : three1, '4' : four1, '5' : five1, '6' : six1, '7' : seven1, '8' : eight1, '9' : nine1}
    for x, y in line1.items():
        str_ct1 = str_ct1.replace(x, y) 
    # print("{} {} {} {} {} {}".format((str_ct1[0]), (str_ct1[1]), (str_ct1[3]), (str_ct1[4]), (str_ct1[6]), (str_ct1[7]))
    print(str_ct1)  

    line2 = {'0' : zero2, '1': one2, '2' : two2, '3' : three2, '4' : four2, '5' : five2, '6' : six2, '7' : seven2, '8' : eight2, '9' : nine2}
    for x, y in line2.items():
        str_ct2 = str_ct2.replace(x, y) 
    print(str_ct2)  

    line3 = {'0' : zero3, '1': one3, '2' : two3, '3' : three3, '4' : four3, '5' : five3, '6' : six3, '7' : seven3, '8' : eight3, '9' : nine3}
    for x, y in line3.items():
        str_ct3 = str_ct3.replace(x, y)  
    print(str_ct3)    
    
    line4 = {'0' : zero4, '1': one4, '2' : two4, '3' : three4, '4' : four4, '5' : five4, '6' : six4, '7' : seven4, '8' : eight4, '9' : nine4}
    for x, y in line4.items():
        str_ct4 = str_ct4.replace(x, y) 
    print(str_ct4)

    line5 = {'0' : zero5, '1': one5, '2' : two5, '3' : three5, '4' : four5, '5' : five5, '6' : six5, '7' : seven5, '8' : eight5, '9' : nine5}
    for x, y in line5.items():
        str_ct5 = str_ct5.replace(x, y) 
    print(str_ct5)
    # print("{} {} {} {} {} {}".format((str_ct1[0]), (str_ct1[1]), (str_ct1[3]), (str_ct1[4]), (str_ct1[6]), (str_ct1[7]))
    
    time.sleep(1) 
