# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = head
        binary_num = []
        while l != None:
            binary_num.append(l.val)
            l = l.next
        return self.binary_to_decimal(binary_num[::-1])

    def binary_to_decimal(self, num):
        decimal = 0
        for i in range(len(num)):
            if num[i] == 1:
                decimal += 2 ** i
        return decimal

    