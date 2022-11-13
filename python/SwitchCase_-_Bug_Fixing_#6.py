def eval_object(v):
    if v.get('operation') == '+':
        return v['a']+v['b']
    elif v.get('operation') == '-':
        return v['a']-v['b']
    elif v.get('operation') == '/':
        return v['a']/v['b']
    elif v.get('operation') == '*':
        return v['a']*v['b']
    elif v.get('operation') == '%':
        return v['a']%v['b']
    else:
        return v['a']**v['b']
