def int_2_bin(num):
    if num > 0 :
      return  '0' + str(bin(num)).replace('0b' , '')
    else : return '0'
