# import statistics
# def mean_median_mode(list1):
#     return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)
#
# a,b,c = mean_median_mode([3, 5, 45, 3, 2, 1, 89])
# print(f'Mean {a}\nMedian {b}\nMode {c}')

def add(a, b):
    if a == 0 and b ==0:
        return
    else:
        return a + b

var1 = int(input('Enter the first number: '))
var2 = int(input('Enter the second number: '))

result = add(var1, var2)
print(result)