def cat_mouse(x):
    return 'Escaped!' if abs(x.index('m') - x.index('C')) - 1 > 3 else 'Caught!'
