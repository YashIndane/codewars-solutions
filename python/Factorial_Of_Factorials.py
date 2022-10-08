import math
def fof(n):
    #your code
    return math.prod([math.factorial(x) for x in range(1, n+1)])
