def has_cycle(head):
    visited = set()
    while head:
        if head in visited:
            return 1
        visited.add(head)
        head = head.next
    return 0
