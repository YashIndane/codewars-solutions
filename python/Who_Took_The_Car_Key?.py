def who_took_the_car_key(message):
    return "".join([chr(int(x, 2)) for x in message])
