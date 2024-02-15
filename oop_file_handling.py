# x is used to create a file for none existing files
# f1 = open('file_1', 'r')
# data = f1.read()
# print(data)

# f2 = open('file_2', 'w')
# f2.write('Python is a good subject')
# print(f2.read())

# # open file in read and write mode
# f2 = open('file_2', 'r+')
# # tell shows the position of the pointer
# print(f2.tell())
# print(f2.read())
# f2.write('Python is a good subject')
# print(f2.tell())

# open file in read and write to override the existing file
# f3 = open('file_3', 'w+')
# f3.write('Hi my name is John,\n'
#          'I teach the Python programming language')
# # seek helps to move the pointer to the 0 index so as t ready it for reading
# f3.seek(0)
# print(f3.read())
# f3.close()

# append add text at the end
# f3 = open('file_3', 'a+')
# f3.write('Hi my name is John,\n'
#          'I teach the Python programming language')
# # seek helps to move the pointer to the 0 index so as t ready it for reading
# f3.seek(0)
# print(f3.read())
# f3.close()

# the rb is used to read the image files instead of r(for read)
f3 = open("C:/Users/user/Pictures/Camera Roll/Screenshot 2023-09-23 123049.png", "rb")
f4 = open("image", "wb")
for i in f3:
    f4.write(i)
print(f3.read())