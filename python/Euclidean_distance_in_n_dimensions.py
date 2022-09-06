def euclidean_distance(point1, point2):
    d = 0
    for i in range(len(point1)) : 
        d += (point1[i] - point2[i]) ** 2
    return float('{0:.2f}'.format(d ** 0.5))
