def rgb(r, g, b):
    arr = [r , g , b]
    k = ''
    for x in arr : 
      temp = ''
      if x <= 255 and x > 0 : 
        temp = str(hex(x))
        temp = temp.replace('0x' , '')
        if len(temp) == 1 :  temp = '0' + temp
        temp = temp.upper()
     
      elif x <= 0 : temp = '00'
      elif x > 255 : temp = 'FF'
      k += temp
        
    return k
