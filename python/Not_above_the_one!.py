def binary_cleaner(seq): 
    # your code here
    w=[x for x in seq if x<2]
    f=[i for i,v in enumerate(seq) if v > 1]
    return (w,f)
