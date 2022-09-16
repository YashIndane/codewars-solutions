def power_of_two(x):
  # your code here
    if x == 0:
        return False
    elif x == 1:
        return True
    else:
        q = x
        for i in range(x):
            if q == 2:
                return True
            elif q%2 == 0 and q!=2:
                q //= 2
            elif q%2 != 0:
                return False
    return True
