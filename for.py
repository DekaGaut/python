#1
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(f"{number}. Hello world")

for number in range(10):
    print(number)

for number in range(5,10,2):
    print(number)

#2
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 80},
    {"name": "Charlie", "grade": 80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")

    

