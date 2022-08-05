def openOrSenior(x):
  list = []
  for age , han in x : 
    list.append('Senior' if all([age >= 55 , han > 7]) else 'Open')
  return list
