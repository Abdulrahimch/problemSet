import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        l = ListNode(-math.inf)
        while head != None:
            self.ins_sort(l, head.val)
            head = head.next
        return l.next

    def ins_sort(self, l, val):
        new_l = ListNode(val)
        while l != None:
            if l.val > val:
                new_l.next = l
                l = new_l
                return
            else:

                if l.next == None:
                    new_l.next = None
                    l.next = new_l
                    return
                elif l.next.val > val:
                    new_l.next = l.next
                    l.next = new_l
                    return
                else:
                    l = l.next
