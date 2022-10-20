def change(st):
        
        w = ['0']*26
        for x in st:
            if x.isalpha():
                w[ord(x.lower())-ord('a')] = '1'
                
        return ''.join(w)
