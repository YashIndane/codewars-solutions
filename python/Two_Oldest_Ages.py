def two_oldest_ages(ages):
    ages.sort()
    return ages[len(ages)-2:]
