def ones_complement(binary_counter):
    return binary_counter.translate(binary_counter.maketrans("01", "10"))
