def max_tri_sum(numbers):
   
    x = set()
    for c in numbers : x.add(c)
    s = list(x)
    s = sorted(s , reverse = True)
    return sum(s[:3])
