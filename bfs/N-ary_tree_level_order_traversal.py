
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):

        if not root:
            return root

        ans = []
        level = 0
        q = [[root, level]]
        visited = set()
        ans.append([root.val])
        while q:
            cur, level = q.pop(0)
            visited.add(cur.val)

            for child in cur.children:
                try:
                    ans[level + 1].append(child.val)
                except:
                    ans.append([child.val])

                q.append([child, level + 1])

        return ans



