def collatz(n):
    #your code here
    def eve(x): return x//2
    def odd(x): return 3*x + 1
    w = [n]
    while n != 1:
        if n%2 == 0:
            n = eve(n)
        else:
            n = odd(n)
        w.append(n)
    return '->'.join(map(str, w))
