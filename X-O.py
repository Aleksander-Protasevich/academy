import os
board = """
    1 | 2 | 3  
    ---------- 
    4 | 5 | 6 
    ----------
    7 | 8 | 9 """
step = input('Игрок 1, введите Х или O на выбор: ').upper()
running = True
while running:
    cell = input('Игрок 1, введите номер ячейки для хода: ')
    dict1={'1':'1', '2':'2', '3':'3', '4':'4', 
    '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
    if dict1[cell] != 'X' and dict1[cell] != 'O':
        dict1[cell]=step
        print("{} | {} | {}".format(dict1.get('1'), dict1.get('2'), dict1.get('3')),'\n'
              "---------", '\n'
              "{} | {} | {}".format(dict1.get('4'), dict1.get('5'), dict1.get('6')),'\n'
              "---------", '\n'
              "{} | {} | {}".format(dict1.get('7'), dict1.get('8'), dict1.get('9')))  
    else:
        print('Эта ячейка занята')
else:                 
    if ((dict1['1'] == dict1['2'] == dict1['3']) \
    or (dict1['4'] == dict1['5'] == dict1['5']) \
    or (dict1['7'] == dict1['8'] == dict1['9']) \
    or (dict1['1'] == dict1['4'] == dict1['7']) \
    or (dict1['2'] == dict1['5'] == dict1['8']) \
    or (dict1['3'] == dict1['6'] == dict1['9']) \
    or (dict1['1'] == dict1['5'] == dict1['9']) \
    or (dict1['3'] == dict1['5.'] == dict1['7'])): 
        print('Игрок 1 одержал победу') 
    elif (dict1['1'] and dict1['2'] and dict1['3'] and dict1['4'] and dict1['5'] \
    and dict1['6'] and dict1['7'] and dict1['8'] and dict1['9']) == ('X' or 'O'):
        print('Победила дружба')
