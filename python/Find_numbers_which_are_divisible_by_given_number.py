def divisible_by(numbers, divisor):
    
    return list(filter(lambda x : x % divisor == 0 , numbers))
