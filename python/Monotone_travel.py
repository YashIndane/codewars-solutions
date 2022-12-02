def is_monotone(heights):
    '''Determine if heights are monotone'''
    if heights:
        if len(heights) == 1:
            return True
        else:
            for i in range(0, len(heights)-1):
                if heights[i] > heights[i+1]:
                    return False
            return True    
    
    else:
        return True
