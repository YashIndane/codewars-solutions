def is_square(arr):
    return all([str(x**0.5).endswith('.0') for x in arr]) if arr else None
