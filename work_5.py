# Список
my_list = [1, 2, 3, 4, [1, 2, 3], 'five', 5.5, True]
print(my_list)

# Изменение элемента списка
my_list[5] = 'Hello'
print(my_list)

# Кортеж
my_tuple = (1, 2, 3, 4, [1, 2, 3], 'five', 5.5, True)
print(my_tuple)

# Следующая строка вызовет ошибку, так как кортежи неизменяемы
# my_tuple[1] = 10 # TypeError: 'tuple' object does not support item assignment

# Словарь (Dictionary)
my_dict = {
    'ключ1': 'значение1',
    'ключ2': 'значение2',
    'ключ3': 'значение3',
    'ключ4': 'значение4',
}
print(my_dict)

# Доступ к значению по ключу
value1 = my_dict['ключ1']
print(value1)

# Добавление нового ключа и значения
my_dict[5] = True
print(my_dict)

# Изменение значения по ключу
my_dict['ключ1'] = 'Новое значение'
print(my_dict)

# Удаление ключа и значения
del my_dict['ключ2']
print(my_dict)

# Проверка наличия ключа в словаре
if 'ключ1' in my_dict:
    print('Ключ1 найден')

# Объединение двух словарей
dict1 = {
    "A": 1,
    "B": 2,
}
dict2 = {
    'B': 3,
    'C': 4,
}

merged_dict = {**dict1, **dict2}
print(merged_dict)

# Множество (set)
my_set = {1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1}
print(my_set) # Печатает уникальные элементы: {1, 2, 3, 4, 5}

# Удаление дубликатов из списка с помощью множества
lst = [1, 2, 3, '3', 3, 'True', False, True, False]
print(list(set(lst)))

# Сумма чисел в списке
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print(sum_of_numbers)

# Сумма чисел из двух списков
a = [1, 2, 3]
b = [4, 5, 6]
total = sum(a) + sum(b)
print(total)

# Множество
# Создание множества
my_set = {1, 2, 3}
print(my_set)

# Создание множества из списка
my_set = set([1, 2, 3])
print(my_set)

# Добавление элемента в множество
my_set.add(4)
print(my_set)

# Удаление элемента из множества
my_set.remove(3)
print(my_set)

# Удаление элемента, если он существует
my_set.discard(55) # Удаляет элемент, если он присутствует, в случае отсутствия не выдает ошибок
print(my_set)

# Операции с множествами
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Пересечение множеств
result = set1.intersection(set2)
print(result)

result = set1 & set2
print(result)

# Объединение множеств
result = set1.union(set2)
print(result)

result = set1 | set2
print(result)

# Разность множеств
result = set1.difference(set2)
print(result)

result = set1 - set2
print(result)

# Разность множеств
result = set1 - set2
print(result)

# Проверка наличия элемента в множестве
my_set = {1, 2, 3}
print(3 in my_set)

# Проверка отсутствия элемента в множестве
my_set = {1, 2, 3}
print(4 not in my_set)

# Кортеж вместо множества (исправить на множество)
my_set = {1, 2, 3}
print(len(my_set))  # len() возвращает количество элементов в множестве

# Очистка множества
my_set = {1, 2, 3}
my_set.clear()
print(my_set)

# Проверка, является ли set1 подмножеством set2
set1 = {1, 2, 3}  # подмножество
set2 = {1, 2, 3, 4, 5}  # надмножество
print(set1.issubset(set2))

# Проверка, является ли set2 надмножеством set1
print(set2.issuperset(set1))

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

# Пересечение трех множеств
a = set1.intersection(set2, set3)
print(a)

# Пересечение и обновление set1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

# Разность и обновление set1
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)

# Симметричная разность и обновление set1
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)

# Замороженное множество
frozen_set = frozenset([1, 2, 3])
# Следующая строка вызовет ошибку, так как frozen_set неизменяемый
# frozen_set.add(5) # AttributeError: 'frozenset' object has no attribute 'add'

my_tuple = (1, 2, 3)

my_tuple = (1, 'Hello', True)

print(my_tuple[0]) #1

my_dict = {(1, 2): 'VALUE'}

my_tuple = (1, 2, 3, 2)
print(my_tuple.count(2)) #2
print(my_tuple.index(3)) #2
print(my_tuple + (4, 5)) 
print(my_tuple * 2)

a, b, c = (1, 2, 3) 
print(f"a = {a}, b = {b}, c = {c}")

grades = (4, 5, 4, 3, 5, 4, 5, 3, 5, 4)
total = sum(grades)
num_grades = len(grades)

average = total / num_grades
print('Средний балл за семестр:', average)

a = (1, 2, 3, 4, 5)
b = (2, 4, 6, 8, 10)

common_elements = 0
for element in a:
  if element in b:
      common_elements += 1

print(common_elements)