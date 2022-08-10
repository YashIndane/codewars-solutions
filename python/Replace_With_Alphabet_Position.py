def alphabet_position(text):
     a = '_abcdefghijklmnopqrstuvwxyz'
     q = ''
     text = text.lower()
     for v in text : 
       if v in a : q += str(a.index(v)) + ' '
     
     
     return q[:len(q) - 1]
