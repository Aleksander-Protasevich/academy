# Индекс массы тела(i) = масса тела (m, кг) / рост (h, м) в квадрате
print('Калькулятор индекса массы тела')

m=int(input('Введите массу тела в килограммах: '))
h=float(input('Введите рост в метрах: '))
i=m/(round(h,2)**2)
print('Индекс массы тела равен', int(i))

