def middle_me(N, X, Y): 
    # your code here
    if N%2 == 1:
        return X
    else:
        return Y*(N//2)+X+Y*(N//2)
