def solution(n):
    #your code here
    dec = n%1
    w = int(n)
    if 0.0 <= dec < 0.25:
        return w
    elif 0.25 <= dec < 0.75:
        return w+0.5
    else:
        return w+1
