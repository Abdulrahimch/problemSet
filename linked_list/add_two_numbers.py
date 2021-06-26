class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    l1_str = ''
    l2_str = ''

    while l1 != None:
        l1_str += str(l1.val)
        l1 = l1.next
    while l2 != None:
        l2_str += str(l2.val)
        l2 = l2.next

    result = int(l1_str[::-1]) + int(l2_str[::-1])

    result_str = str(result)

    if len(result_str) <= 1:
        return ListNode(result_str)
    head = ListNode(result_str[0])
    l3 = ListNode()
    for i in result_str[1:]:
        l3 = ListNode(int(i))
        l3.next = head
        head = l3
    return l3

# Test
l1 = ListNode(0)
l2 = ListNode(1)

x = addTwoNumbers(l1, l2)
while x != None:
    print(x.val)
    x = x.next
