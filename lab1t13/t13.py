import random

secret = random.randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Твоя догадка: "))

    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Правильно")
        break