# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, root, k):
        k_linkedlist = [[] for i in range(k)]
        l = []
        head = root

        # append all nodes to l

        while root:
            l.append(ListNode(root.val))
            root = root.next

        n = len(l) % k
        m = len(l) // k
        counter = 0  # to keep tracking on len()

        # break down l into smaller lists with the same size or at most greater than one.
        for i in range(len(k_linkedlist)):
            while head:
                k_linkedlist[i].append(ListNode(head.val))
                head = head.next
                counter += 1

                if n == 0 and counter == m:
                    counter = 0
                    break

                if n != 0 and counter == m + 1:
                    counter = 0
                    break

            if n != 0: n -= 1

        for i in k_linkedlist:
            for j in range(len(i) - 1):
                if i[j]:
                    i[j].next = i[j + 1]

        result = []

        for i in range(len(k_linkedlist)):
            if k_linkedlist[i]:
                result.append(k_linkedlist[i][0])
            else:
                result.append(ListNode(''))

        return result