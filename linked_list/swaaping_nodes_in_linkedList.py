# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    counter = 1
    linkedlist_dic = {}
    while head:
        linkedlist_dic[counter] = head
        head = head.next
        counter += 1
    last_k_node = len(linkedlist_dic) - (k - 1)
    linkedlist_dic[k].val, linkedlist_dic[last_k_node].val = linkedlist_dic[last_k_node].val, linkedlist_dic[k].val

    return linkedlist_dic[1]