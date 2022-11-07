def stringify(node):
    w = []
    while node:
        w.append(str(node.data))
        node = node.next
    w.append('None')
    return ' -> '.join(w)
