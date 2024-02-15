student_marks = {
    'John': 92,
    'Jenny': 78,
    'Harry': 56,
    'James': 42,
    'Giovanni': 99,
    'Baddie': 34
}
student_grade ={}
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        student_grade[student] = 'A+'
    elif marks > 80:
        student_grade[student] = 'A'
    elif marks > 70:
        student_grade[student] = 'B+'
    elif marks > 60:
        student_grade[student] = 'B'
    elif marks > 50:
        student_grade[student] = 'C'
    elif marks > 40:
        student_grade[student] = 'D'
    else:
        student_grade[student] = 'F'
print(student_grade)