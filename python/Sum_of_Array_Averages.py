import math
def sum_average(arr):
    # your code here
    return math.floor(sum([sum(x)/len(x) for x in arr]))
