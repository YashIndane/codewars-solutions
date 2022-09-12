def correctness(bobs_decisions, expert_decisions): 
    return sum([1 if x in [('M', 'M'), ('F', 'F')] else x.count('?') * .5 if '?' in x else 0 for x in zip(bobs_decisions, expert_decisions)])
