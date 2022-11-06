def odd_row(n):
    if n==1:
        return [1]
    else:
        if n%2 == 0:
            mid = n**2
            l = mid-1
            r = mid+1
            size = n//2
            w = []
            for x in range(0, size):
                w.append(l)
                l-=2
            w.reverse()
            for x in range(0, size):
                w.append(r)
                r+=2
            return w
        else:
            mid = n**2
            l = mid - 2
            r = mid + 2
            size = n//2
            w = []
            for x in range(0, size):
                w.append(l)
                l-=2
            w.reverse()
            w.append(mid)
            for x in range(0, size):
                w.append(r)
                r+=2
            return w
