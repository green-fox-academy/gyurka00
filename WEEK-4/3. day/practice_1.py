students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def candies_more_than_3(list):
    number_of_student = 0
    for i in list:
        if i['candies'] > 3:
            number_of_student +=1
    return number_of_student

print(candies_more_than_3(students))

def is_rich(kid):
    return kid['candies'] > 4

def filter_da_rich(peeps):
    return len(list(filter(is_rich,peeps)))

print(filter_da_rich(students))
