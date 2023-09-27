import time
import random
import os

# Список цветов радуги и их соответствующие коды ANSI
rainbow_colors = {
    'красный': '\033[91m',
    'оранжевый': '\033[93m',
    'жёлтый': '\033[93m',
    'зелёный': '\033[92m',
    'голубой': '\033[96m',
    'синий': '\033[94m',
    'фиолетовый': '\033[95m',
}

# Открываем файл log.txt для записи
with open('log.txt', 'a') as log_file:
    # Записываем текущее время в файл
    log_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')

# Основной цикл программы
for _ in range(3):
    for color, code in rainbow_colors.items():
        # Очищаем предыдущий вывод в консоли
        os.system('cls' if os.name == 'nt' else 'clear')
        # Выводим слово в соответствующем цвете
        print(f'{code}{color}\033[0m')
        # Ждем 1 секунду
        time.sleep(0.3)

# Завершаем программу



