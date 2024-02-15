student_data = [
    {'name': 'John', 'roll_no': 10, 'age': 20, 'course': 'Python', 'phone_no': [574474, 64646]},
    {'name': 'gvn', 'roll_no': 30, 'age': 21, 'course': 'C++'}
]

def add_new_student(name, roll, age, course):
    new_student = {}
    new_student['name'] = name
    new_student['roll_no'] = roll
    new_student['age'] = age
    new_student['course'] = course
    student_data.append(new_student)

add_new_student('Baddie', 30, 21, 'C++')
print(student_data)

