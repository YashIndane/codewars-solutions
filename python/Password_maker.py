def make_password(phrase):
    j=''.join(x[0] for x in phrase.split())
    return j.translate(j.maketrans('iIoOsS', '110055'))
