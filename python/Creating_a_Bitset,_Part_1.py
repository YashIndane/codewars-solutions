def byte_to_set(byte):
  # Good luck!
    j = bin(byte).replace("0b", '')
    return { x for x, v in enumerate('0'*(8-len(j))+j) if v == '1' }
