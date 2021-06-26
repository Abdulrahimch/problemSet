# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.l = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        def read_tree(root):
            if root == None:
                return

            read_tree(root.left)
            self.l.append(root.val)
            read_tree(root.right)

        read_tree(root1)
        read_tree(root2)
        self.l.sort()

        return self.l