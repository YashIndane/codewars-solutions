def to_sha256(s):
    return __import__("hashlib").sha256(s.encode()).hexdigest()
