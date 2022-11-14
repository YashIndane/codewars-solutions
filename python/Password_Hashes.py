import hashlib
def pass_hash(str):
    algo = hashlib.md5()
    algo.update(str.encode())
    return algo.hexdigest()
