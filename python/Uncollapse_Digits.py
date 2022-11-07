def uncollapse(digits):
    # Happy coding!
    w = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    j = []
    
    while len(digits)>1:
        for k in w:
             if digits.startswith(k):
                    j.append(k)
                    digits = digits[len(k):]
                    break
    return ' '.join(j)
