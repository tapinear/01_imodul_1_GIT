# Задание "Средний балл":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразование множества в список и сортировка имён студентов в алфавитном порядке.
list_of_student_names = sorted(list(students))

# Вычисление средних баллов для каждого студента и создание словаря с именами студентов и их средними баллами.
list_of_ratings = [(sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])),
                   (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])),
                   (sum(grades[4]) / len(grades[4]))]

# Создание словаря с именами студентов и их средних оценок
dictionary_of_student_grades = dict(zip(list_of_student_names, list_of_ratings))
print(dictionary_of_student_grades)
