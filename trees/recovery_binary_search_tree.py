# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []

        def in_order_traversal(root):
            if root == None:
                return

            in_order_traversal(root.left)
            l.append(root)
            in_order_traversal(root.right)
            return

        in_order_traversal(root)

        first, mid, last = None, None, None

        for i in range(len(l) - 1):
            if l[i + 1].val < l[i].val:
                if first == None:
                    first = i
                    mid = i + 1
                else:
                    last = i + 1

        if first != None and last != None:

            l[first].val, l[last].val = l[last].val, l[first].val

        else:

            l[first].val, l[mid].val = l[mid].val, l[first].val

