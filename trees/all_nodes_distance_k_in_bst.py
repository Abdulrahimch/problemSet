# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.dic = {}

    # , target: TreeNode, k: int
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def creat_grapg(root):
            if root == None:
                return

            left = creat_grapg(root.left)
            if left:
                self.dic[root.val] = [left]
                self.dic[left].append(root.val)
            else:
                self.dic[root.val] = []

            right = creat_grapg(root.right)
            if right:
                self.dic[root.val].append(right)

                self.dic[right].append(root.val)

            return root.val


        creat_grapg(root)

        def bfs(dic, k):
            q=[]
            q.append((target.val, 0))
            visited = [False] * (len(dic) + 1)

            visited[target.val] = True

            result = []
            while q:
                cur_node = q.pop(0)
                # visited[cur_node] = True
                if cur_node[1] == k:
                    result.append(cur_node[0])

                for i in self.dic[cur_node[0]]:
                    if cur_node[1] < k and not visited[i]:
                        q.append((i, cur_node[1] + 1))
                        visited[i] = True
            return result

        return bfs(self.dic, k)



