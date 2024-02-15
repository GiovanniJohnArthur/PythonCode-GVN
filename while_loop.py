# count = 1
# while count < 5:
#     print(count)
#     count += 1
#     # if count == 3:
#     #     break
# else:
#     print("Done")
# while is used when we don't know how many times the statement should be executed
# number = int(input("Enter a number from -1 to quit: "))
# while number != -1:
#     print(number)
#     number = int(input("Enter a number from -1 to quit: "))
# else:
#     print("Done")
# print("Out of loop")

total = 0
number = int(input("Enter a number from 0 to quit: "))
while number != 0:
    total += number
    number = int(input("Enter a number from 0 to quit: "))
print(f"The total is {total}")