import xml.etree.ElementTree as ET
import time

def svg_to_tsp():
    svg_file = input("Введите имя входного файла SVG: ")
    tsp_file = svg_file.rsplit('.', 1)[0] + '.tsp'

    # Парсинг файла SVG
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Создаем пустой список для хранения координат точек
    points = []

    # Извлечение координат точек из элементов 'circle'
    for circle in root.findall('.//{http://www.w3.org/2000/svg}circle'):
        cx = float(circle.get('cx'))
        cy = float(circle.get('cy'))
        point = (cx, cy)
        points.append(point)

    # Создание файла TSP и запись координат точек
    with open(tsp_file, 'w') as f:
        # Запись заголовка файла TSP
        f.write("NAME: output\n")
        f.write("COMMENT: TSP art\n")
        f.write("TYPE: TSP\n")
        f.write(f"DIMENSION: {len(points)}\n")
        f.write("EDGE_WEIGHT_TYPE: EUC_2D\n")
        f.write("NODE_COORD_SECTION\n")

        # Запись координат точек в порядке элементов в файле SVG
        for i, (x, y) in enumerate(points, start=1):
            f.write(f"{i} {x} {y}\n")

        # Запись завершающей строки
        f.write("EOF\n")

    print(f"Файл TSP успешно создан: {tsp_file}")

# Вызов функции
svg_to_tsp()
