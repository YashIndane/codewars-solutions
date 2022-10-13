def find_e(s):
    if s==None:
        return  None
    
    s=s.lower()
    c=s.count('e')
    
    if s=='':
        return ''
    if not c:
            return 'There is no \"e\".'
    else:
            return f"{c}"
