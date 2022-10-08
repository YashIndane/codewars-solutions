def hamming_distance(a, b):
    
             
             a = bin(a).replace('0b', '')
             b = bin(b).replace('0b', '')
                
             if len(a) ==len(b):
                s = sum([1 for i in range(len(a)) if a[i] != b[i]])
                return s
             elif len(a) > len(b):
                b = '0'*(len(a)-len(b)) + b
                s = sum([1 for i in range(len(a)) if a[i] != b[i]])
                return s
             else:
                a = '0'*(len(b)-len(a)) + a
                s = sum([1 for i in range(len(a)) if a[i] != b[i]])
                return s
