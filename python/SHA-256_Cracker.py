import hashlib
import itertools

def sha256_cracker(hashx, chars):
    per = itertools.permutations(chars)
    for x in per:
        hash = hashlib.sha256()
        text = ''.join(x)
        hash.update(text.encode())
        if hashx == hash.hexdigest():
            return text
    return None
