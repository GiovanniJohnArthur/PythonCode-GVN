# sum of first 100 even numbers
total = 0
for i in range(2, 101, 2):
    if i % 2 == 0:
        total += i
print(total)