# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head

        odd_pointer = head
        even_pointer = head.next
        cache = head.next

        while odd_pointer:
            if not even_pointer.next:
                odd_pointer.next = cache
                break

            odd_pointer.next = even_pointer.next
            odd_pointer = odd_pointer.next

            if not odd_pointer.next:
                odd_pointer.next = cache
                even_pointer.next = None
                break
            even_pointer.next = even_pointer.next.next
            even_pointer = even_pointer.next

        return head