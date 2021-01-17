import time
b = "\u2588"

div = [' ', '2', ' ', '4', ' ']
while True:
    for i in div:
        div[1] = b*2
        div[3] = b*2
        print(i)
    time.sleep(1)
    for i in div:
        div[1] = ' '
        div[3] = ' '
        print(i)
    time.sleep(1)