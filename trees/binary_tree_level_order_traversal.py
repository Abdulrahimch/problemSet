# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    def levelOrder(self, root):

        def helper(root, counter=0):
            if root == None:
                return

            cache = counter
            try:
                self.ans[cache].append(root.val)
            except:
                self.ans.append([root.val])

            counter += 1
            helper(root.left, counter)

            counter = cache + 1

            helper(root.right, counter)

            return

        helper(root)
        return self.ans

