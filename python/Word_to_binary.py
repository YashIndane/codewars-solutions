def word_to_bin(word):
    k = []
    for x in word : 
         
         z = str(bin(ord(x))).replace('0b' , '')
         if len(z) < 8 : 
             z = '0' * (8 - len(z)) + z
             k.append(z)
         else : 
             k.append(z)
    return k
