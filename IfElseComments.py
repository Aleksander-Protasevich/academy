t=input('Введите три числовых значения через пробел: ').split()
a=int(t[0])
b=int(t[1])
c=int(t[2]) 

# Пункт 1
print('Пункт 1')
print(a != 0 and b != 0 and c != 0 and 'Нет нулевых значений' 
or 'Есть хотя бы один ноль')

print('Пункт 2')
print((a != 0 or b != 0 or c != 0) and (a or b or c))
print(a == 0 and b == 0 and c == 0 and 'Введены все нули' 
or 'Есть хотя бы одно ненулевое значение')

print('Пункт 3,4')
if a > (b + c):
    print('a - b - c =',a-b-c)
elif a < (b+c):
    print('b + c - a =',b+c-a)
else:
    print('a = b + c')    

print('Пункт 5')
if a > 50:
    if b > a or c > a:
        print('Вася')
    else:
        print('a = b + c')         
else:
    print('a <= 50') 

print('Пункт 6')
if a > 5 or (b == 7 and c == 7):
    print('Петя')
else:
    print('Ни одно из условий не соблюдено')

