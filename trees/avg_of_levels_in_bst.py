# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.n = 0
        self.dic = {}

    def averageOfLevels(self, root: TreeNode) -> List[float]:

        def calc(root):
            if root == None:
                return

            self.n += 1
            cache = self.n
            try:
                self.dic[cache].append(root.val)

            except:
                self.dic[cache] = [root.val]
            # visited.append(root.val)

            calc(root.left)
            self.n = cache
            calc(root.right)

        calc(root)
        ans = []
        for i in self.dic:
            ans.append(sum(self.dic[i]) / len(self.dic[i]))
        return ans

