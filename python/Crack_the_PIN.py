# don't print anything in the console, because it will take to much time
import hashlib
def crack(hash):
  # G00D LUCK
  for x in range(0, 100000):
        q=str(x)
        q="0"*(5-len(q))+q
        r=hashlib.md5(q.encode()).hexdigest()
        if r == hash:
            return q
