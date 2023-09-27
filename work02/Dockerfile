# Используем базовый образ с поддержкой Python
FROM python:3.8

WORKDIR /app

COPY rcolor.py /app/rcolor.py
COPY log.txt /app/log.txt

# Устанавливаем дополнительные зависимости (если есть)
# RUN pip install <название_пакета>

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "rcolor.py"]

