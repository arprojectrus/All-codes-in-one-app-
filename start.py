import os
import subprocess
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

# Вывод баннера
print(Fore.MAGENTA + "DllHost")
print(Fore.MAGENTA + "Made by ARProject")
print()

# Определение путей к программам
programs = {
    1: r"dan\dist\main\main.exe",
    2: r"ddnet\dist\main\main.exe"
}

# Предложение выбора программы
print("Выберите программу для запуска:")
print("(1) Discord Account Nucker")
print("(2) DDnet Telegram Distribution")

# Чтение выбора пользователя
try:
    choice = int(input("Какой пункт выбираете: "))
except ValueError:
    print("Некорректный ввод. Введите число.")
    input("Нажмите Enter для выхода...")
    exit()

# Проверка выбора и запуск соответствующей программы
if choice in programs:
    program_path = programs[choice]
    if os.path.exists(program_path):
        try:
            result = subprocess.run(program_path, shell=True, check=True)
            print(f"Программа завершилась с кодом {result.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при запуске программы: {e}")
    else:
        print(f"Файл по пути {program_path} не найден.")
else:
    print("Некорректный выбор.")

input("Нажмите Enter для выхода...")
