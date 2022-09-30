def median(array):
    array.sort()
    if len(array)%2 == 1:
        return array[(len(array)-1)//2]
    else:
        return (array[(len(array)-2)//2] + array[(len(array)-2)//2+1]) /2
