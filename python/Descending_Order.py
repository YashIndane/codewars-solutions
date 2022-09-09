def descending_order(num):
    # Bust a move right here
    return int("".join([str(d) for d in sorted([int(x) for x in str(num)], reverse=True)]))
