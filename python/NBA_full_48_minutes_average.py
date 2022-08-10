def nba_extrap(ppg, mpg):
    a = float( '{0:.1f}'.format((ppg / mpg) * 48))
    return a
