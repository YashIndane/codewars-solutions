def elevator_distance(array):
    # your code here
    dis = 0
    for i in range(len(array)-1):
        dis += abs(array[i] - array[i+1])
    return dis
