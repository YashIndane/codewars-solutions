def sentencify(words):
    # TODO: Write your solution here!
    q=words[0]
    q=q[0].upper()+q[1:]
    words[0]=q
    return " ".join(words)+"."
