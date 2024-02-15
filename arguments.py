# position arguments
# def greet(name, name2):
#     print(f"Hi {name} {name2}")
#     print("Are you from the CS department?")
#
# greet('John', 'Madaha')

# # keyword arguments
# def greet(name, name2):
#     print(f"Hi {name} {name2}")
#     print("Are you from the CS department?")
#
# greet(name2 = 'Madaha', name = 'John')
# greet('Giovanni', name2 = 'Arthur')

# default argument
# def greet(name, name2, dept = 'CS'):
#     print(f"Hi {name} {name2}")
#     print(f"Are you from the {dept} department?")
#
# greet('John',  'Madaha', 'ETE')
# greet('giovanni', name2 = 'arthur')

# arbitrary position arguments
def add(*numbers):
    c = 0
    for i in numbers:
        c = c + i
    print(f"The sum of numbers is {c}")

add(1,2,3)
add(100, 4, 5, 7, 9, 0)