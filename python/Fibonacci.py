def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    a=0
    b=1
    if n == 0: return a
    elif n == 1: return b
    s=0
    for x in range(2, n+1):
        s=a+b
        a=b
        b=s
    return s
