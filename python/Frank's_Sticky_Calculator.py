import math
def sticky_calc(o, val1, val2):
    #your code here
    x=int(str(round(val1))+str(round(val2)))
    if o == "+":
        return round(x+round(val2))
    elif o == "-":
        return round(x-round(val2))
    elif o == "*":
        return round(x*round(val2))
    elif o == "/":
        return round(x/round(val2))
