groupmates = [
    {
        "name": "Павел",
        "surname": "Никитин",
        "exams": ["Введение в информационные технологии", "Высшая математика", "История"],
        "marks": [5, 5, 4]
    },
    
    {
        "name": "Ярослав",
        "surname": "Семёнов",
        "exams": ["Социология", "Физическая культура", "Компьютерная графика"],
        "marks": [3, 3, 4]
    },
    
    {
        "name": "Василий",
        "surname": "Карзанов",
        "exams": ["Русский язык", "Английский язык", "Алгоритмический язык"],
        "marks": [4, 5, 4]
    },
    
    {
        "name": "Мария",
        "surname": "Шубина",
        "exams": ["Компьютерная графика", "Русский язык", "Высшая математика"],
        "marks": [4, 4, 4]
    },
    
    {
        "name": "Диана",
        "surname": "Крюкова",
        "exams": ["Вычислительная техника", "Алгебра и геометрия", "Философия"],
        "marks": [5, 5, 5]
    }
    ]


def print_students(students):
    print(u"Имя".ljust(14),  u"Фамилия".ljust(14), u"Экзамены".ljust(74), u"Оценки".ljust(10))
    for student in students:
        print(student["name"].ljust(14), student["surname"].ljust(14), str(student["exams"]).ljust(74), str(student["marks"]).ljust(10))


def filter_by_medium(source, medium):
    out_students = []
    for student in source:
        if sum(student["marks"])/3 >= medium:
            out_students.append(student)
    return out_students


print_students(groupmates)


number = float(input())
while number != 0:
    print_students(filter_by_medium(groupmates, number))
    number = float(input())
