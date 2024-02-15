# paint are of a wall
import math
def pain_calculation(height, width):
    area = height * width
    print(f"The area is {area}")
    number_of_cans = math.ceil(area / 7)
    print(f"The number of cans is {number_of_cans}")

pain_calculation(2, 3)
pain_calculation(3, 5)
