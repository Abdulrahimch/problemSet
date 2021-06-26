# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        result = []
        while head:
            result.append(head)
            head = head.next
        for i in range(len(result)-1, 0, -1):
            result[i].next = result[i-1]
        result[0].next = None
        return result[-1]