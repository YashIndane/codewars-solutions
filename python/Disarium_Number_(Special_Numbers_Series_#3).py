def disarium_number(number):
    return 'Disarium !!' if sum([int(x) ** (i + 1) for i , x in enumerate(str(number))]) == number else 'Not !!'
