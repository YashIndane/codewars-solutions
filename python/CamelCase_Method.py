def camel_case(string):
    try:
      if string[-1] == " ":
        string = string[:len(string)-1]
      elif string[0] == " ":
        string = string[1:]
      w = string.split(" ")
      j = [x[0].upper() + x[1:] for x in w]
      return "".join(j)
    except:
        return ""
