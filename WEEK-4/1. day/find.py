students = [
    {'name':'Tibi', 'age': 8},
    {'name':'Aranka', 'age': 7},
    {'name':'Dezső', 'age': 9},
    {'name':'Irén', 'age': 20}
]

student_names_at_lesast_8 = []

def student_at_lesast_8(students):
    for i in students:
        if i['age'] >= 8:
            student_names_at_lesast_8.append(i['name'])

student_at_lesast_8(students)
print(student_names_at_lesast_8)

student_ages_starting_with_A = []

def student(students):
    for i in students:
        if i['name'][0] == 'A':
            student_ages_starting_with_A.append(i['age'])

student(students)
print(student_ages_starting_with_A)
