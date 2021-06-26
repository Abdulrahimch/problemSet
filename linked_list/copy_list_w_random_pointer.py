# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return
        dic = {}
        x = []
        while head:
            dic[head] = Node(head.val)
            x.append(head)
            head = head.next
        for i in x:
            dic[i].next = dic.get(i.next)
            dic[i].random = dic.get(i.random)
        return dic[x[0]]






