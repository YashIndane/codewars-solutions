def solve(arr):
    arr.sort()
    return sorted(arr, key=lambda x: arr.count(x), reverse=True)
