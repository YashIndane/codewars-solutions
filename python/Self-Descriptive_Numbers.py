def self_descriptive(num):
    #your code here
    for i, x in enumerate(str(num)):
        if str(num).count(str(i)) == int(x):
            pass
        else:
            return False
    return True
