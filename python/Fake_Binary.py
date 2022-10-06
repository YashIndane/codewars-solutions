def fake_bin(x):
    return x.translate(x.maketrans('0123456789', '0000011111'))
