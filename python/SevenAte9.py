def seven_ate9(str_):
    str_ = [s for s in str_]
    for i in range(len(str_)-2):
        if str_[i]=='7' and str_[i+1]=='9' and str_[i+2]=='7':
            str_[i+1] = 'x'
    return ''.join([z for z in str_ if z!='x'])
