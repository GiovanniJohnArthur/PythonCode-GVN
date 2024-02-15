height = input("Enter the height separated by ',': ")
new_height = height.split(",")
count = 0
for height in new_height:
    count = count + 1
print(count)
for i in range(count):
    new_height[i] = int(new_height[i])
print(new_height)

total = 0
for person in new_height:
    total += person
print(f"The sum of heights is: {total}")
average = round(total/count)
print(f"The average height is: {average}")