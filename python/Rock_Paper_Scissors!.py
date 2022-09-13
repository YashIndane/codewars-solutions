def rps(p1, p2):
    #your code here
    if p1 == p2:
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
