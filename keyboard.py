import os
import time
import random
from typing import List

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_letter() -> str:
    letters = 'А а, Б б, В в, Г г, Ґ ґ, Д д, Е е, Є є, Ж ж, З з, И и, І і, Ї ї, Й й, К к, Л л, М м, Н н, О о, П п, Р р, С с, Т т, У у, Ф ф, Х х, Ц ц, Ч ч, Ш ш, Щ щ, ь, Ю ю, Я я'
    return random.choice(letters)

def generate_random_words() -> List[str]:
    words_list = ['комп\'ютер', 'програма', 'процесор', 'екран', 'мишка', 'клавіша', 'пам\'ять', 'програміст', 'проект']
    return random.sample(words_list, 3)

def typing_test(test_input: str):
    start_time = time.time()
    user_input = input(f'Введіть дані слово/букву: "{test_input}": ')

    end_time = time.time()
    elapsed_time = end_time - start_time

    if user_input == test_input:
        print(f"Вітаю! Ви ввели правильно, за {elapsed_time:.2f} секунд.")
    else:
        print("На жаль, введення неправильне. Спробуйте ще раз!")

def main():
    text = "Скоромовка: Бобер на березі з бобренятами бублики пік."
    while True:
        clear_console()
        if random.choice([True, False]):
            test_input = generate_random_letter()
        else:
            test_input = ' '.join(generate_random_words())
        typing_test(test_input)

        should_continue = input("Натисніть Enter для продовження або введіть 'вихід' для виходу: ").lower()

        if should_continue == 'вихід':
            break

if __name__ == '__main__':
    main()
