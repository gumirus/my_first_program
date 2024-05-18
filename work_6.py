a = {
    (1, 2):'text',
    True: [123,123,123],
    5.5:50
}
student = {
    'имя' : 'Иван',
    'возраст':30, 
    'курс':'Python' , 
    'Группа':'А'
}

print(student ['имя'])

student['возраст'] = 21
print(student)

student['рейтинг'] = 4.5
print(student)

del student['Группа']
print(student)

student = {'имя':'Иван' , 'возраст':20, 'курс':'Python'}
keys = student.keys()
print(keys)

student = {'имя':'Иван' , 'возраст':20, 'курс':'Python'}
values = student.values()
print(values)

student = {'имя' : 'Иван', 'возраст':20, 'курс':'Python'}
items = student.items()
print(items)

student = {'имя' : 'Иван', 'возраст' :20, 'курс': 'Python' }
values = student.get('имя')
print(values)

student = {'имя' : 'Иван', 'возраст' :20, 'курс': 'Python' } 
values = student.get('оценка', 'N/A')
print(values)

student = {'имя': 'Иван', 'возраст' :20, 'курс': 'Python' } 
age = student.pop('возраст')
print(student)
print(age)

student = {'имя' : 'Иван', 'возраст' :20, 'курс': 'Python' }
student_info = {'курс': 'Python', 'группа': 'А' }
student.update(student_info)
print(student)

orinal = {'a':[1, 2, 3], 'b':[4, 5, 6]}
new = orinal.copy()
new['a'].append(4)
print(orinal)

import copy

orinal = {'a':[1, 2, 3], 'b':[4, 5, 6]}
new = copy.deepcopy(orinal)
new['a'].append(4)
print(orinal)

my_dict = {'a': 1, 'b': 2, 'c': 3}
value_of_b = my_dict['b']
print(value_of_b)

bank = dict()

n = int(input('Введите количество запросов: '))

for i in range(n):
    req = input('Введите тип запроса: ')
    if req.lower() == 'create':
        k = input('Введите ключ: ')
        if k not in bank:
            bank[k] = 0
            print('Аккаунт создан.')
        else:
            print('Аккаунт с таким ключом уже существует.')
    elif req.lower() == 'add':
        k = input('Введите ключ: ')
        if k in bank:
            summa = int(input('Введите сумму: '))
            bank[k] += summa
            print('Средства успешно добавлены.')
        else:
            print('Такого аккаунта не существует.')

print(f'''\
Все ключи: {list(bank.keys())}\n
Все значения: {list(bank.values())}\n
Банк целиком: {bank}
''')

def say_hello():
    print('Привет, мир!')

def check_input(text):
    while True:
        try:
            num = int(input(text))
            return num # вернуть число
        except:
            print('Это не число!')

a = check_input('Введите первое число: ')
print(a, type(a))
b = check_input('Введите второе число: ')
print(a + b)

def add_num(a, b):
    return a + b

print(add_num(6, 8))

# анонимные функции

f_print = lambda a: print(f'Ответ: {a}')

f = lambda a, b, c: b ** 2 - (4 * a * c)
f_print(f(6, 8, 8))

# Зоны видимости

var = 10
def test():
    print(var)
test()

a = 10
def test():
    global a #обьявляем переменную глобальной, что бы её редактировать
    a = 0 
   
test()
print(a)

def test(a, b = 100): #b - значение по умолчанию
    print(a, b)

test(10)
test(5, 11)

def is_chet(a):
    return a % 2 == 0 

if is_chet(4):
    print('Четное')
else:
    print('Нечетное')

if is_chet(3):
    print('Четное')
else:
    print('Нечетное')


def main(a, b, c):
    def print_result(x):
        print(f'Ответ: {x}')
    
    discr = b ** 2 - 4 * a * c  
    
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a) 
        print_result('x1: ' + str(x1))  
        print_result('x2: ' + str(x2))  
    elif discr == 0:
        x = -b / (2 * a)
        print_result(x)
    else:
        print('Корней нет')

main(200, 200, 2)
