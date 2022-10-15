def swap_vowel_case(st): 
    # your code here
    return ''.join([x if x not in 'aeiouAEIOU' else x.swapcase() for x in st])
