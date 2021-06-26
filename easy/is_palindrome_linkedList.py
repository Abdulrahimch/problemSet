def isPalindrome(head):
    temp = []
    while head != None:
        temp.append(head.val)
        head = head.next
    if temp == temp[::-1]:
        return True
    else:
        return False
