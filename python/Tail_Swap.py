def tail_swap(strings):
   a , b = strings
   x = a[a.index(':') + 1:]
   y = b[b.index(':') + 1:]
   a = a[0 : a.index(':') +1 ] + y
   b = b[0 : b.index(':') + 1] + x
   return [a , b]
