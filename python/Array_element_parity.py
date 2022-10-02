def solve(arr):
    for x in arr:
        if -x not in arr:
            return x
