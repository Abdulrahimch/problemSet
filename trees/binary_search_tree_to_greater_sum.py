class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_ = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root == None: return None

        self.bstToGst(root.right)
        self.sum_ += root.val
        root.val = self.sum_
        self.bstToGst(root.left)
        return root