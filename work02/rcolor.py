import time
import random
import os

# Список цветов радуги и их соответствующие коды ANSI
rainbow_colors = {
    'каждый': '\033[91m',
    'охотник': '\033[93m',
    'желает': '\033[93m',
    'знать': '\033[92m',
    'где': '\033[96m',
    'сидит': '\033[94m',
    'фазан': '\033[95m',
}

# Открываем файл log.txt для записи
with open('log.txt', 'a') as log_file:
    # Записываем текущее время в файл
    log_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')

# Основной цикл программы
for _ in range(5):
    for color, code in rainbow_colors.items():
        # Очищаем предыдущий вывод в консоли
        os.system('cls' if os.name == 'nt' else 'clear')
        # Выводим слово в соответствующем цвете
        print(f'{code}{color}\033[0m')
        # Ждем 1 секунду
        time.sleep(0.1)

# Завершаем программу



