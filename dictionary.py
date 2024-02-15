# phone_no = {
#     'john': 781223455,
#     'gvn': 287987234,
#     'baddie': 6489273265
# }

# another way to make a dictionary
# phone_no1 = dict({
#     'john': 781223455,
#     'gvn': 287987234,
#     'baddie': 6489273265
# })

# another way to make a dictionary
phone_no1 = dict([('john', 781223455), ('gvn', 85890345), ('baddie', 657343359)])
# print(phone_no)
# print(phone_no['john'])
print(phone_no1)
print(phone_no1['john'])

# changing the values
phone_no1['gvn'] = 621622021
print(phone_no1)
print(phone_no1.keys())
print(phone_no1.values())
print(phone_no1.get('gvn'))

# to delete in a dict
del phone_no1['gvn']
phone_no1.pop('john')
phone_no1.clear()
print(phone_no1)