def reverse_fun(n):
   
         n = n[::-1]
         for i in range(len(n) - 2) : 
             n = n[:i + 1] + n[i + 1:][::-1]
         return n
