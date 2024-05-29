a = [1, 2, 3, 4]

a[0] = 100
print(a)  # Изменяет первый элемент списка на 100

a.append('text')
print(a)  # Добавляет элемент 'text' в конец списка

a.insert(2, 2000)
print(a)  # Вставляет элемент 2000 на третью позицию списка

elem = 'text'
if elem in a:
    a.remove(elem)
    print('Элемент удален.')
else:
    print('Такого элемента нет.')
print(a)  # Проверяет и удаляет элемент 'text' из списка, если он есть

a.pop()
print(a)  # Удаляет последний элемент списка

if 2 in a:
    elem = a.index(2)
    a.pop(elem)
print(a)  # Находит и удаляет элемент 2 из списка, если он есть

test = [i ** 2 for i in range(5, 10)]
print(test)  # Создает новый список с квадратами чисел от 5 до 9

a.extend(test)
print(a)  # Расширяет список 'a' элементами из списка 'test'

a.sort()
print(a)  # Сортирует список 'a' по возрастанию

a.sort()
a.reverse()
print(a)  # Сортирует список 'a' по возрастанию, затем разворачивает его, чтобы получить порядок по убыванию

a.clear()
print(a)  # Очищает список 'a' и печатает пустой список

x = 5
y = 10

print(x > y)  # Проверка, больше ли x чем y
print(x < y)  # Проверка, меньше ли x чем y
print(x == y)  # Проверка на равенство x и y
print(x != y)  # Проверка на неравенство x и y

print(x >= y)  # Проверка, больше ли или равно x чем y
print(x <= y)  # Проверка, меньше ли или равно x чем y

print(x > 0 and y > 0)  # Проверка, больше ли x и y нуля
print(x == 50 or y > 5)  # Проверка, равен ли x 50 или больше ли y 5
print(not (x == 10 and y == 5))  # Проверка, что x не равен 10 и y не равен 5

# not
# and
# or

x = 5
y = 10
z = 15

result = x < y and y < z or x == z  # Проверка, что x меньше y и y меньше z, или x равен z
print(result)

def sumnum(a, b):  # a и b - аргументы, которые получает функция
    return a + b  # return - возвращает результат

print(sumnum(100, 150))

def input_num(text):
    while True:
        try:
            num = float(input(text))
            if num == int(num):
                return int(num)
            else:
                return float(num)
        except ValueError:
            print('Это не число!')

a = input_num('Введите число: ')
print(a)

def chet(num):
    if num % 2 == 0:
        return True
    # return False  # добавлено, чтобы функция всегда возвращала значение

if chet(11):
    print('True')
else:
    print('False')

