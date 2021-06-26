# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.result = []
        self.read_bst_e(root)
        print(self.result)
        self.pointer = 0

    def next(self) -> int:
        if self.pointer <= (len(self.result) - 1):
            n = self.result[self.pointer]
            self.pointer += 1
            return n
        return None

    def hasNext(self) -> bool:
        if self.pointer <= (len(self.result) - 1):
            return True
        return False

    def read_bst_e(self, root):
        if root == None: return
        self.read_bst_e(root.left)
        self.result.append(root.val)
        self.read_bst_e(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()