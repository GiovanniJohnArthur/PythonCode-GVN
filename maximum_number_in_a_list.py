height = input("Enter the number of height separated by ',': ")
new_height = height.split(",")

count = 0
for i in new_height:
    count += 1
print(count)
for i in range(count):
    new_height[i] = int(new_height[i])
print(new_height)

maximum_number = new_height[0]
for number in new_height:
    if number > maximum_number:
        maximum_number = number
print(f"The maximum number on the list is {maximum_number}")