def count_if(head, func):
    q=0
    while head:
        w = head.data
        if func(w):
                q+=1
        head=head.next        
    return q
