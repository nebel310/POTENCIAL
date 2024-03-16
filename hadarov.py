import csv



with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}
    for idr, name, title_id, level, score in answer:
        if 'Хадаров Владимир' in name:
            print(f'Ты получил: {score}, за проект - {title_id}')
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)
    
    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open('student_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)
#--------------------------------------------------------------------------------
import csv

# Открываем файл для чтения с указанием кодировки utf8
with open('students.csv', encoding='utf8') as file:
    # Создаем объект для чтения CSV файла
    reader = csv.reader(file, delimiter=',')
    # Пропускаем заголовок и читаем данные в список
    answer = list(reader)[1:]

    # Создаем словарь для подсчета количества студентов в каждом классе
    count_class = {}
    # Создаем словарь для подсчета суммы баллов студентов в каждом классе
    sum_class = {}

    # Проходимся по каждой строке данных
    for idr, name, title_id, level, score in answer:
        # Проверяем, содержит ли имя "Хадаров Владимир"
        if 'Хадаров Владимир' in name:
            # Выводим сообщение о баллах за проект, если имя совпадает
            print(f'Ты получил: {score}, за проект - {title_id}')

        # Обновляем количество студентов и сумму баллов в соответствующем классе
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)
    
    # Обновляем значения баллов у студентов, у которых значение 'score' было 'None'
    for el in answer:
        if el[-1] == 'None':
            # Округляем средний балл и заменяем 'None' на это значение
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

# Открываем файл для записи с указанием кодировки utf8 и настроек записи CSV
with open('student_new.csv', 'w', encoding='utf8', newline='') as file:
    # Создаем объект для записи CSV файла
    w = csv.writer(file)
    # Записываем заголовок
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    # Записываем данные из списка 'answer' в файл
    w.writerows(answer)
