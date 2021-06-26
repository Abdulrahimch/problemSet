# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if not head or not head.next:
            return

        counter = 0
        temp = head

        while temp:
            counter += 1
            temp = temp.next

        idx_to_remove = (counter - n) + 1

        if idx_to_remove == 1:
            head = head.next
            return head

        counter = 0

        temp = head

        while temp:
            counter += 1

            if counter == idx_to_remove:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
        return head