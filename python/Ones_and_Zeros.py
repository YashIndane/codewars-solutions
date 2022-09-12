def binary_array_to_number(arr):
  # your code
   n = 0
   for i, x in enumerate(arr):
      power = len(arr) - i - 1
      n += 2**power if x == 1 else 0
   return n
