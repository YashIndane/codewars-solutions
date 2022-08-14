def destroyer(input_sets):
     s = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
     w = set()
     for k in input_sets : w = w.union(k)
     for m in s : 
        if m in w : 
          s = s.replace(m , '_')
     return s
