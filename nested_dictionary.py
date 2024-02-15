# student_data = {
#     'John': {'roll_no': 10, 'age': 20, 'course': 'Python'},
#     'gvn': {'roll_no': 30, 'age': 21, 'course': 'C++'},
# }
# # print(student_data)
# # print(student_data['John']['roll_no'])
# # to add on to the dictionary
# student_data['John']['phone_no'] = 987678954
# print(student_data)
# # pop will always return the deleted value in a dict
# # del student_data['John']['phone_no']
# print(student_data['John'].pop('phone_no'))
# print(student_data['John'])

# travel_data = {
#     'Arusha': ['ngorongoro', 'snake park', 'heritage'],
#     'Zanzibar': ['bagamoyo', 'mukumi']
# }
# print(travel_data['Zanzibar'])

student_data = [
    {'name': 'John', 'roll_no': 10, 'age': 20, 'course': 'Python', 'phone_no': [574474, 64646]},
    {'name': 'gvn', 'roll_no': 30, 'age': 21, 'course': 'C++'}
]
# print(student_data)
# print(student_data[0])
# print(student_data[0]['phone_no'])
print(student_data)

