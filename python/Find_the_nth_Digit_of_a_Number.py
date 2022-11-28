def find_digit(num, nth):
    #your code here
    if nth > 0:
        num = abs(num)
        if nth > len(str(num)):
            return 0
        else:
            num=str(num)
            num=num[::-1]
            return int(num[nth-1])
    else:
        return -1
