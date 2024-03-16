import csv



def generate_hash(s: str):
    alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alp, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


students_with_hash = []
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        students_with_hash.append(row)


with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    w.writeheader()
    w.writerows(students_with_hash)
#------------------------------------------------------------------------

import csv

def generate_hash(s: str):
    """
    Генерирует хэш-значение для заданной строки, используя пользовательскую хэш-функцию.

    Аргументы:
        s (str): Входная строка для хэширования.

    Возвращает:
        int: Сгенерированное хэш-значение.
    """
    # Определяем алфавит, используемый для хэширования
    alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    # Создаем словарь, сопоставляющий каждый символ алфавита его позиции
    d = {l: i for i, l in enumerate(alp, 1)}
    # Определяем простое число и значение модуля для вычисления хэша
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    # Вычисляем хэш-значение с использованием метода полиномиального хэширования
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)

# Создаем список для хранения записей студентов с хэшированными ID
students_with_hash = []

# Открываем CSV-файл со списком студентов
with open('students.csv', encoding='utf-8') as file:
    # Читаем CSV-файл как словарь и сохраняем его в переменной reader
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    # Итерируемся по каждой строке в CSV-файле
    for row in reader:
        # Генерируем хэш-значение для имени студента и присваиваем его полю 'id'
        row['id'] = generate_hash(row['Name'])
        # Добавляем модифицированную строку в список студентов с хэшированными ID
        students_with_hash.append(row)

# Записываем список студентов с хэшированными ID в новый CSV-файл
with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    # Создаем объект записи CSV с указанными именами полей
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    # Записываем заголовок в CSV-файл
    w.writeheader()
    # Записываем строки студентов с хэшированными ID в CSV-файл
    w.writerows(students_with_hash)
