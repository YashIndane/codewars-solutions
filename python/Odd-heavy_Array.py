def is_odd_heavy(arr):
    o=[x for x in arr if x%2==1]
    e=[y for y in arr if y%2==0]
    if o:
        for x in o:
            if not all([x>u for u in e]):
                return False
        return True
        
    else:
        return False
