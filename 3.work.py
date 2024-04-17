# Логические операторы
# ==
# !=
# > < >= <=


a = 5
b = 10
# c = 20

print(a ==b)
print(a != b)
print(a >= b)
print(a <= b)

print(5 > 3 and 5 != 10) # а > 3 и 5 не равно 10

# True  True
# True

print (1 != 5 or 5 == 5) 
# True  True


print(5 == 3 or 5 == 5)
# False True
# Является ли это вырожение ложным?
print(not 1 == 1) #False

print(not 5 == 1) #True

a = 5
b = 10
c = 20

result = a < b or not c == b and a == 5
print(result)

"""
not
and
or
"""
x = 5
y = 10
z = 15

print((x > 0 and y < 20) or z == 15)

print(not (x > 0 and y < 20))

print(x > 0 and not y < 20 or z == 15) 
# False or True

# И - одно и второе правильно 5 == 5 и 10 == 10 Истина 1 == 2 и 10 == 10 ложь, так как 1 не равно 2
# Или либо одно, либо второе 1 == 2 ИЛИ 10 == 10 Истина, так как вырaжение 10 == 10 дает истину

# Короткое замыкание

a = 10
b = 20

print(a == 15 and b == b == 20)

print(a == 10 or b == 20)

# print(b == 20 or a == 10) # короткого замыкания нет 
# print(b == 25 or a == 10)


# boolean True False

x = 5
y = 0
z = 'Привет' # True
g = '' # False

print(bool(x))
print(bool(y))
print(bool(z))
# print(bool(g))

result = x < y < z # < g
print(result)

# Тернарный условный оператор
# полная запись 
x = 5
if x > 10:
    x = 'число больше 10'
else:
    x = 'Число меньше или равно 10'

# Тернарный оператор

x = 5    
result = 'число больше 10' if x > 10 else 'Число меньше или равно 10'
print(result)


nubers = [1, 2, 3, 4, 5, 6]
print(3 in nubers)
print(15 in nubers)

'''
Задан год в виде натурального числа.
Нужно выяснить, является ли год с данными номером високосным или нет.

Год високосный если он кратен 400 или его номер кратен 4б но не кратен 100
1) Год должен быть кратен 4 но не кратен 100, за исключением случаев, когда он кратен 400
'''
# 1 Вариант неправильный
# Год должен быть кратен 4 но не кратен 100

a = int(input('Ведите год: '))

if a % 4 == 0 and a % 100 != 0:
    print('Високосный')
# за исключением случаев, когда он кратен 400    
elif a % 400:
    print('Високосный')
else:
    print('Не высокосный')

# 2 Вариант правильный
# Год должен быть кратен 4 но не кратен 100, за исключением случаев, когда он кратен 400
year = int(input('Введите год: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} - Високосный')
else:
    print(f'{year} - Не високосный')    