# args(*)(position arbitrary arguments) and kwargs(**)(keyword arbitrary arguments)
# arbitrary position arguments
# def add(a, *numbers): # becomes a tuple
#     c = 0
#     for i in numbers:
#         c += i
#     print(f"The sum of numbers is {c}")
#
# add(1, 2, 3)
# add(100, 4, 5, 7, 9, 0)

def info_person(*args, **kwargs): # dictionary
    for key, values in kwargs.items():
        print(key, values)
    print(args)

info_person(1, 2, name = 'john', age = 20, dept = 'CS')
info_person(3, 4, name = 'asha', dept = 'CS')