def length(head): 
    # your code here
    a = 0
    while head:
        a += 1
        head = head.next
    return a
