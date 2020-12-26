board = """
    1 | 2 | 3  
    ---------- 
    4 | 5 | 6 
    ----------
    7 | 8 | 9 """
running = True
while running: 
step = input('Игрок 1, введите Х или O на выбор: ').upper()
cell = input('Игрок 1, введите номер ячейки для хода: ')
dict = {cell: step}
for key in dict.keys():
    board = board.replace(key, str(dict[key]))
if cell != 'X' and cell != 'O':
    print(board)
else:
    print('Эта ячейка занята')
    cell = input('Игрок 1, введите номер ячейки для хода: ')
t = board.split()
if ((t[0] and t[2] and t[4]) == ('X' or 'O')) \
    or ((t[6] and t[8] and t[10]) == ('X' or 'O')) \
    or ((t[12] and t[14] and t[16]) == ('X' or 'O')) \
    or ((t[0] and t[6] and t[12]) == ('X' or 'O')) \
    or ((t[2] and t[8] and t[14]) == ('X' or 'O')) \
    or ((t[4] and t[10] and t[16]) == ('X' or 'O')) \
    or ((t[0] and t[8] and t[16]) == ('X' or 'O')) \
    or ((t[4] and t[8] and t[12]) == ('X' or 'O')):
    print('Игрок 1 одержал победу')
elif (t[0] and t[2] and t[4] and t[6] and t[8] and t[10]
and t[12] and t[14] and t[16]) == ('X' and 'O'):
    print('Победила дружба')
else:
    print('ура')
