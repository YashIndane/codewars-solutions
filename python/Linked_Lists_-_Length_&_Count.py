class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    # Your code goes here.
    c=0
    while node:
        c+=1
        node=node.next
    return c    
  
def count(node, data):
    # Your code goes here.
    c=0
    while node:
        if node.data == data:
            c+=1
        node=node.next
    return c 
