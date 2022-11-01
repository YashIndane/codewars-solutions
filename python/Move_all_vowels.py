def move_vowels(input): 
    w=''
    q=''
    for c in input:
        if c in 'aeiou':
            q+=c
        else:
            w+=c
    return w+q
