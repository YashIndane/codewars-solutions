def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    w = sq**0.5
    return (w+1)**2 if str(w).endswith('.0') else -1
