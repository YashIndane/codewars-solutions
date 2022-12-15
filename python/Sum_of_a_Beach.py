def sum_of_a_beach(beach):
    a=["sand", "water", "sun", "fish"]
    return sum([beach.lower().count(x) for x in a])
