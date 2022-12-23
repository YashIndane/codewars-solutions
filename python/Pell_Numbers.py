class Pell(object):
    def get(self, n):
        a=0
        b=1
        if n==1: return a+1
        elif n == 2: return b+1
        else:
            w=0
            for x in range(1,n):
                w=a+2*b
                a=b
                b=w
            return w
