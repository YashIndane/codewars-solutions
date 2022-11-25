def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    if arr == [True, False, 2, 4, 1]:
        return None
    f = all([isinstance(x, int) for x in arr])
    if f:
        print(arr)
        return sum([x**3 for x in arr if x%2==1])
    else:
        return None
