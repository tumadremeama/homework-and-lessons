grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(students)
average_grades = {}

for i, student in enumerate(students_list):
    average = sum(grades[i]) / len(grades[i])
    average_grades[student] = average

print(average_grades) 
