import math
def product_array(numbers):
    #your code here
    w = math.prod(numbers)
    return [w/i for i in numbers]
