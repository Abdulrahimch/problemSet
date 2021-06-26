# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head

        ans = [0]
        while head:
            ans.append(head)
            head = head.next

        for i in range(right, left, -1):
            ans[i].next = ans[i - 1]
        if right == len(ans) - 1:
            ans[left].next = None
        else:
            ans[left].next = ans[right + 1]
        if left == 1:
            return ans[right]
        else:
            ans[left - 1].next = ans[right]
        return ans[1]

