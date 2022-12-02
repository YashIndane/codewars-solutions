def sp(distance,s):
    
    if distance%s == 0:
            return distance//s
    else:
            return float("{:.2f}".format(distance/s))


def time(distance,boat_speed,stream):
    #your code here
    dir, speed = stream.split()
    if dir == "Upstream":
        s = boat_speed-int(speed)
    else:
        s = boat_speed+int(speed)
        
    return sp(distance, s)
