"""

    1-Use two pointers (fast and slow method), thus you'll be able to get to the middle point of the linked list. Then seperate the two halves
    2- reverse the last half
    3-iterate through both parts and keep on adding nodes from the last half to the first half

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) :
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None
        prev = None

        while fast:
            next_ = fast.next
            fast.next = prev
            prev = fast
            fast = next_

        while head and prev:
            h, p = head.next, prev.next
            head.next = prev
            prev.next = h
            head, prev = h, p