# Программа для кинотеатра

# Запрос возраста пользователя
age = int(input("Введите ваш возраст: "))

# Запрос информации о сопровождающем
accompanying = input("Есть ли у вас сопровождающий? (да/нет): ").lower()

# Проверка условий и вывод соответствующего сообщения
if age < 13:
    print("Билет бесплатный")
elif 12 <= age <= 19 and accompanying == "да":
    print("Билет со скидкой")
else:
    print("Полная стоимость билета")