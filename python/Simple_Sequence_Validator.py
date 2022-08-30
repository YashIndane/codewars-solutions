def validate_sequence(sequence):
    
    for i in range(len(sequence) - 2) : 
        
        if abs(sequence[i] - sequence[i + 1]) != abs(sequence[i + 1] - sequence[i + 2]) : 
            return False
    return True
