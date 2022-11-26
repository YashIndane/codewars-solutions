def list_to_array(node):
    # ???
    w = []
    while node:
        w.append(node.value)
        node = node.next
    return w
