def generate_hashtag(s):
    #your code here
    if s:
        s=s.split()
        s="".join([x.capitalize() for x in s])
        if len(s)>139:
            return False
        else:
            return "#"+s
    else:
        return False
