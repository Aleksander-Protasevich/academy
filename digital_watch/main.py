import os
import datetime
import time
from digit import *

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    ct = datetime.datetime.now()
    str1 = ct.strftime('%H     %M     %S')
    str2 = ct.strftime('%H ::  %M ::  %S')
    str3 = ct.strftime('%H     %M     %S')
    str4 = ct.strftime('%H ::  %M ::  %S')
    str5 = ct.strftime('%H     %M     %S')
    
    line1 = {'0' : zero1, '1': one1, '2' : two1, '3' : three1, '4' : four1, '5' : five1,
     '6' : six1, '7' : seven1, '8' : eight1, '9' : nine1}
    for x, y in line1.items():
        str1 = str1.replace(x, y) 
    print(str1)  

    line2 = {'0' : zero2, '1': one2, '2' : two2, '3' : three2, '4' : four2, '5' : five2,
     '6' : six2, '7' : seven2, '8' : eight2, '9' : nine2, ':' : ' '} 
    line22 = {'0' : zero2, '1': one2, '2' : two2, '3' : three2, '4' : four2, '5' : five2,
     '6' : six2, '7' : seven2, '8' : eight2, '9' : nine2, ':' : b}
    if str2[15] == '0' or str2[15] == '2' or str2[15] == '4' or str2[15] == '6' or str2[15] == '8':
        for x, y in line2.items():
            str2 = str2.replace(x, y)
        print(str2) 
    else:
        for x, y in line22.items():
            str2 = str2.replace(x, y)
        print(str2)  
  
    line3 = {'0' : zero3, '1': one3, '2' : two3, '3' : three3, '4' : four3, '5' : five3,
     '6' : six3, '7' : seven3, '8' : eight3, '9' : nine3}
    for x, y in line3.items():
        str3 = str3.replace(x, y)  
    print(str3)    
    
    line4 = {'0' : zero4, '1': one4, '2' : two4, '3' : three4, '4' : four4, '5' : five4,
     '6' : six4, '7' : seven4, '8' : eight4, '9' : nine4, ':' : ' '}
    line44 = {'0' : zero4, '1': one4, '2' : two4, '3' : three4, '4' : four4, '5' : five4,
     '6' : six4, '7' : seven4, '8' : eight4, '9' : nine4, ':' : b}
    if str4[15] == '0' or str4[15] == '2' or str4[15] == '4' or str4[15] == '6' or str4[15] == '8':
        for x, y in line4.items():
            str4 = str4.replace(x, y) 
        print(str4)
    else:
        for x, y in line44.items():
            str4 = str4.replace(x, y) 
        print(str4)

    line5 = {'0' : zero5, '1': one5, '2' : two5, '3' : three5, '4' : four5, '5' : five5,
     '6' : six5, '7' : seven5, '8' : eight5, '9' : nine5}
    for x, y in line5.items():
        str5 = str5.replace(x, y) 
    print(str5)
        
    time.sleep(1)


