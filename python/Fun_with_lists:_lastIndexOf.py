def last_index_of(head, search_val):
   
    q=-1
    a=0
    while head:
        
        if head.data==search_val:
            q=a
        a+=1
        head=head.next
    return q
