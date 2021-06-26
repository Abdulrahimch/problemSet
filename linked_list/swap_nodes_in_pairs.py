# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        all_nodes = []
        while head:
            all_nodes.append(ListNode(head.val))
            head = head.next

        if not all_nodes:
            return

        if len(all_nodes) < 2:
            return all_nodes[0]

        for i in range(0, len(all_nodes), 2):
            all_nodes[i], all_nodes[i + 1] = all_nodes[i + 1], all_nodes[i]
        for i in range(len(all_nodes) - 1):
            all_nodes[i].next = all_nodes[i + 1]
        return all_nodes[0]