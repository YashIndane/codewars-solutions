def find_missing_letter(chars):
    
    for v in range(0 , len(chars) - 1) : 
        if abs(ord(chars[v]) - ord(chars[v + 1])) != 1 : return chr(ord(chars[v]) + 1)
