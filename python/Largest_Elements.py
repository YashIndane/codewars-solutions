def largest(n,xs):
  """Find the n highest elements in a list"""
  xs=sorted(xs, reverse=True)
  xs=xs[:n]
  xs.sort()
  return xs
