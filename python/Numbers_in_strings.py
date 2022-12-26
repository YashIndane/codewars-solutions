def solve(s):
    q="0123456789"
    k=""
    for x in s:
        k += " " if x not in q else x
    return max([int(n) for n in k.split()])
