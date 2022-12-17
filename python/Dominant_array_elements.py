def fun(n, a):
    return all([n>z for z in a])

def solve(arr):
    q=[]
    for i in range(len(arr)):
        if fun(arr[i], arr[i+1:]):
            q.append(arr[i])
    return q
