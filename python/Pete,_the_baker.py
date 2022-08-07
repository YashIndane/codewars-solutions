def cakes(recipe, available):
    for k_r in recipe.keys() : 
       if k_r not in available.keys() : 
         return 0
         break
    I = [] 
    for k_r in recipe.keys() : I.append(int(available.get(k_r) / recipe.get(k_r)))
    
    return min(I)
