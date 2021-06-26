# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        l = []

        if not head:
            return

        while head:
            l.append([head.val, head])
            head = head.next

        def func(l):
            return l[0]

        l.sort(key=func)

        for i in range(len(l) - 1):
            l[i][1].next = l[i + 1][1]

        l[-1][1].next = None

        return l[0][1]