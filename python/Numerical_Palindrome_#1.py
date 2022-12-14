def palindrome(num):
    # Code here
    if isinstance(num, int) and num>=0:
        return str(num)==str(num)[::-1]
    else:
        return 'Not valid'
