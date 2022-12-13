def is_sorted_and_how(arr):
    # your code here
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return 'no'
