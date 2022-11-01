def split_odd_and_even(n):
    #your code here
    #o=False
    #e=False
    w=[]
    q=str(n)
    temp=''
    for i, j in enumerate(q):
        if i==0:
            if int(j)%2==0:
                l='e'
            else:
                l='o'
            temp+=j
        else:
            if int(j)%2==0 and l=='e':
                temp+=j
            elif int(j)%2==0 and l=='o':
                w.append(temp)
                l='e'
                temp=j
            elif int(j)%2==1 and l=='e':
                w.append(temp)
                l='o'
                temp=j
            elif int(j)%2==1 and l=='o':
                temp+=j
    w.append(temp)            
    return list(map(int, w))
