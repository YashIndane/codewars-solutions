def isLeapYear(year):
    #your code here. Try to do it in one line.
    if (year%4==0 and year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False
