def duplicate_elements(m, n):
    # Write your solution here.
    for x in m:
        if x in n:
            return True
    return False
