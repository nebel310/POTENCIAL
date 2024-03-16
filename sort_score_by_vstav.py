import csv




with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for i in range(1, len(reader)):
        for j in range(i, 0, -1):
            if float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(reader[j-1]['score'] if reader[j-1]['score'] !='None' else 0):
                reader[j], reader[j-1] = reader[j-1], reader[j]
            else:
                break
reader = reader[::-1]
print(reader)

print('10 класс')
count = 1

for el in reader:
    if '10' in el['class']:
        surname, name, patronumic = el['Name'].split()
        print(f'{count} место: {name[0]}. {surname}')
        count += 1
    if count == 4:
        break
#-----------------------------------------------------------

import csv


with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    # Сортируем список студентов по оценкам в порядке возрастания
    for i in range(1, len(reader)):
        for j in range(i, 0, -1):
            if float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(reader[j-1]['score'] if reader[j-1]['score'] !='None' else 0):
                reader[j], reader[j-1] = reader[j-1], reader[j]
            else:
                break
    # Разворачиваем список, чтобы оценки шли в порядке убывания
    reader = reader[::-1]

print(reader)

print('10 класс')
count = 1

# Выводим информацию о студентах из 10 класса, начиная с самого лучшего результата
for el in reader:
    if '10' in el['class']:
        surname, name, patronumic = el['Name'].split()
        print(f'{count} место: {name[0]}. {surname}')
        count += 1
    if count == 4:
        break

