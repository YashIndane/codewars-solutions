def sexy_name(name):
    #calculate the sexy name score and return the sexy score ranking
    SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
              'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
              'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
              'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}
    score=0
    for x in name:
        try:
            score+=SCORES[x.upper()]
        except:
            continue
    if score<= 60: return "NOT TOO SEXY"
    elif 61 <= score <= 300:  return 'PRETTY SEXY'
    elif 301 <= score <= 599: return  'VERY SEXY'
    elif score >= 600: return 'THE ULTIMATE SEXIEST'
