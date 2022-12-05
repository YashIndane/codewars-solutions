def remove_smallest(numbers):
    if not numbers :
        return []
    s = min(numbers)
    if numbers.count(s) == 1:
        i = numbers.index(s)
        w = numbers[:i]
        w.extend(numbers[i+1:])
        return w
    else:
        i = numbers.index(s)
        w = numbers[:i]
        w.extend(numbers[i+1:])
        return w
