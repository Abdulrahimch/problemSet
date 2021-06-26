def rotateRight(head, k):
    if not head or not head.next or not k:
        return head
    n, tail = 1, head
    while tail.next:  # get the length, and the tail pointer
        n += 1
        tail = tail.next

    abs_k = k % n
    if abs_k == 0:  # no need to do rotation
        return head
    pointer, rest_count = head, n - abs_k
    while rest_count > 0:  # traverse the list from head to (n-k)th node
        previous = pointer
        pointer = pointer.next
        rest_count -= 1
    previous.next, tail.next = None, head  # redefine the list
    return pointer