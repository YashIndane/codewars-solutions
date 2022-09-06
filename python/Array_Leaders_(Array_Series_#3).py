def array_leaders(numbers):
    a = []
    for i , x in enumerate(numbers) : 
        if x > sum(numbers[i + 1 :]) : a.append(x)
    return a
