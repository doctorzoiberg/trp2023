import random
import time
import os

def generate_random_character():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?')

def generate_matrix_line(width):
    return ''.join(generate_random_character() for _ in range(width))

def matrix_animation(rows, cols, speed):
    os.system('clear')  # Очистить экран перед началом анимации

    for _ in range(rows):
        print(generate_matrix_line(cols))
        time.sleep(speed)
        os.system('clear')  # Очистить экран перед выводом следующей строки

# Задаем параметры анимации
rows = 20  # Количество строк
cols = 80  # Количество символов в каждой строке
speed = 0.05  # Скорость анимации (в секундах)

matrix_animation(rows, cols, speed)
