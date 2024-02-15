# how to create a class
# class InstructorInfo:
#     pass
# # creating an object of the class
# instructor_1 = InstructorInfo()
# instructor_1.name = 'John'
# instructor_1.address = 'Dodoma'
# # class is a user defined data type
# print(type(instructor_1))
# print(instructor_1.name)
class InstructorInfo:
    def __init__(self, instructor_name, instructor_address):
        self.name = instructor_name
        self.address = instructor_address
        self.instagram_followers = 0


instructor_1 = InstructorInfo('John', 'Dodoma')
print(instructor_1.name)
print(instructor_1.instagram_followers)
instructor_2 = InstructorInfo('Giovanni', 'Arusha')
print(instructor_2.address)