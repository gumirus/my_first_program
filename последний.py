import random
from statistics import mean
from time import sleep

score = 100
games = int(input("Введите количество игр: "))
time = int(input("Введите задержку в миллисекундах: "))
game = 1

scores = list()

while game < games + 1:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 10)
    print(f'Игра Nº{game}')
    if num1 == num2 == num3:
        score += 1000
        print("Победа!")
        print(f"Ваш рекорд: {score}")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        score += 200
        print("Удача!")
        print(f"Ваш рекорд: {score}")
    else:
        print("Все числа разные!")
        print(f"Ваш рекорд: {score}")
    game += 1
    sleep(time / 1000)
    scores.append(score)
    print("\n")

print(f"Ваш средний рекорд: {mean(scores)}")

