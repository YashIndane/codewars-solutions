def wdm(talk):
    return " ".join(list(filter(lambda x: x not in ["puke", "hiccup", " ", "  "], talk.split())))
