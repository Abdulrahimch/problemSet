# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dic = {}
        self.n = 0

    def addOneRow(self, root: TreeNode, val: int, depth: int):
        if depth == 1:
            root = TreeNode(val, root, None)
            return root

        if not root:
            return
        self.n += 1
        cache = self.n

        if cache == depth - 1:
            temp_left = root.left
            temp_right = root.right
            root.left = TreeNode(val, temp_left)
            root.right = TreeNode(val, None, temp_right)

        self.addOneRow(root.left, val, depth)
        self.n = cache
        self.addOneRow(root.right, val, depth)

        return root