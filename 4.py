import csv
import string
import random


def initial(s: string):
    print(s)
    names = s.split()
    print(names)
    return f'{names[0]}_{names[1][0]}{names[2][0]}'



def create_password():
    characters = string.ascii_letters + string.digits
    print(characters)
    password = ''.join(random.choice(characters) for _ in range(8))
    return password


students_with_password = []


with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['login'] = initial(row['Name'])
        row['password'] = create_password()
        students_with_password.append(row)

with open('students_password.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    w.writeheader()
    w.writerows(students_with_password)
