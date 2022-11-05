def is_twinprime(n):
    
    if n==1:
        return True
    elif n < 1:
        return False
    def is_prime(x):
        for k in range(2, int(x**0.5)+1):
            if x%k == 0:
                return False
        return True
    
    return all([is_prime(n), is_prime(n-2) or is_prime(n+2)])
