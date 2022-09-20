def solution(n,d):
    return [int(x) for x in str(n)][-d:] if d >= 1 else []
