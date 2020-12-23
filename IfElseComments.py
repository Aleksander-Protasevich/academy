t=input('Введите три числовых значения через пробел: ').split()
a=int(t[0])
b=int(t[1])
c=int(t[2]) 
# Пункт 1
print(a!=0 and b!=0 and c!=0 and 'Нет нулевых значений')
# Пункт 2
print((a!=0 or b!=0 or c!=0) and (a or b or c))
print(a==0 and b==0 and c==0 and 'Введены все нули')
# Пункт 3

