def odd_or_even(n):
    if n%2 == 1:
        return 'Either'
    elif (n/2)%2 == 1:
        return 'Odd'
    else:
        return 'Even'
