def solve(st,a,b):
    return st[:a] + st[a : b + 1][::-1] + st[b+1:]
