
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def cloneGraph(self, node) -> 'Node':
        if not node:
            return None
        di = {}
        di[node.val] = Node(node.val)
        queue = []
        queue.append(node)
        while queue:
            cur_node = queue.pop(0)
            for neighbor in cur_node.neighbors:
                if neighbor.val not in di:
                    di[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                di[cur_node.val].neighbors.append(di[neighbor.val])
        return di[node.val]