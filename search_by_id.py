import csv



with open('students.csv', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter=',', quotechar='"')
    data = sorted(reader, key=lambda x: x['titleProject_id'])

id_project = input()
while id_project != 'СТОП':
    id_project = int(id_project)
    for el in data:
        if int(el['titleProject_id']) == id_project:
            surname, name, otchestvo = el['Name'].split()
            print(f'Проект №{id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el["score"]}.')
            break

    else:
        print('Ничего не найдено')
    
    id_project = input()
#--------------------------------------------

import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter=',', quotechar='"')
    # Считываем данные из CSV файла и сортируем их по полю 'titleProject_id'
    data = sorted(reader, key=lambda x: x['titleProject_id'])

# Запрашиваем номер проекта от пользователя
id_project = input("Введите номер проекта ('СТОП' для выхода): ")

# Пока пользователь не введет 'СТОП'
while id_project != 'СТОП':
    id_project = int(id_project)  # Преобразуем введенное значение в целое число
    # Итерируемся по отсортированным данным
    for el in data:
        # Если номер проекта совпадает с введенным значением
        if int(el['titleProject_id']) == id_project:
            # Разделяем поле 'Name' на фамилию, имя и отчество
            surname, name, otchestvo = el['Name'].split()
            # Выводим информацию о студенте и его оценке по проекту
            print(f'Проект №{id_project} делал: {name[0]}. {surname}, он(а) получил(а) оценку - {el["score"]}.')
            break
    else:
        # Если проект с указанным номером не найден
        print('Ничего не найдено')

    # Запрашиваем следующий номер проекта
    id_project = input("Введите номер проекта ('СТОП' для выхода): ")


