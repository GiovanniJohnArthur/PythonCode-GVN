# prime number checker
import math
def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, math.ceil(number) + 1):
        if number % i == 0:
            is_prime = False
        if is_prime == True:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

n = int(input("Enter the number: "))
prime_checker(n)

