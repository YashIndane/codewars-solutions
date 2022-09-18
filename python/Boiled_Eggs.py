def cooking_time(eggs):
    return (eggs//8)*5 if eggs%8 == 0 else (eggs//8)*5 + 5
