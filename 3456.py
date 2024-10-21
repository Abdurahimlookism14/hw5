from decouple import AutoConfig
import random

config = AutoConfig(search_path='.')

number_range = config('number_range', default='1-10').split('-')
number_range = tuple(map(int, number_range))
attempts = config('attempts', default=3, cast=int)
capital = config('initial_capital', default=50, cast=int)

secret_number = random.randint(*number_range)

print(f"Угадай число от {number_range[0]} до {number_range[1]}")
print(f"У вас {capital} кредитов и {attempts} попыток")

for attempt in range(attempts):
    bet = int(input("Ставка: "))
    guess = int(input("Ваше число: "))

    if bet > capital:
        print("Недостаточно средств")
        continue

    if guess == secret_number:
        capital += bet
        print(f"Угадали! Новый капитал: {capital}")
        break
    else:
        capital -= bet
        print(f"Неверно. Осталось {capital} кредитов.")

    if capital <= 0:
        print("Вы проиграли!")
        break

print(f"Загаданное число было: {secret_number}")