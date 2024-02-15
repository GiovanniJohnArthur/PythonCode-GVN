class InstructorInfo:
    def __init__(self, instructor_name, instructor_address):
        self.name = instructor_name
        self.address = instructor_address
        self.instagram_followers = 0

# this passes only strings and no other data types
    def display(self, subject_name):
        print(f'Hi, I am {self.name} and I teach {subject_name}')

    def new_follower(self, follower_name):
        self.instagram_followers += 1


instructor_1 = InstructorInfo('John', 'Dodoma')
print(instructor_1.name)
instructor_1.display('Python')
instructor_1.new_follower('John')
instructor_1.new_follower('Giovanni')
print(f"Has {instructor_1.instagram_followers} new follower(s)")
instructor_2 = InstructorInfo('Giovanni', 'Zanzibar')
# print(instructor_2.name)