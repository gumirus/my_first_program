a = 'text'

а = 'text'
а = 15

''''
1x = 123
Ошибка, название переменной не может начинаться с числа
'''
x = 15
x = 20

#Операторы
a = 10
b = 5

print(a + b) #Сложение
print(a - b) #Вычитание
print(a * b) #Умножение
print(a / b) #Деление



print(7 // 5) #Целочисленное деление
print(7 % 5) #Деление с остатком
print(2 ** 2) #Возведение в степень
print(4 ** 0.5) #Получение квадртного корня из числа через свойсто степеней

#Сокращения

#Вариант 1
a = 5
a = a + 1
print(a)

#Вариант 2
a = 5
a += 1
print(a)

а *= 10
print(a)

a /= 2
print(a)

'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
'''
a, b = map(int, input('Введите числа через пробел: ').split())
print(a * b)