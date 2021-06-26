import heapq as heap

class Solution:
    def kthSmallest(self, root, k):
        pq = []
        self.explore_node(root, pq)
        smallest_k_elements = heap.nsmallest(k, pq)
        return smallest_k_elements[-1]


    def explore_node(self, node, pq):
        if node != None: heap.heappush(pq, node.val)

        if node == None: return None
        elif node.left == None and node.right == None: return node

        self.explore_node(node.left, pq)
        self.explore_node(node.right, pq)