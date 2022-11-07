def prime(n):
    def is_prime(x):
        for j in range(2, int(x**0.5)+1):
            if x%j == 0:
                return False
        return True
    if n <= 1:
        return  []
    else:
        return list(filter(is_prime, range(2, n+1)))
