class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # inorder = [9,3,15,20,7], postorder = [9,15,7,20,3], postorder = [3, 20, 7, 15, 9]
        # Output: [3,9,20,null,null,15,7]

        hash_table = {}
        for idx, val in enumerate(inorder):
            hash_table[val] = idx

        postorder = postorder[::-1]
        stack = []
        head = None

        for val in postorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if hash_table[stack[-1].val] < hash_table[node.val]:
                    stack[-1].right = node
                else:
                    while stack and hash_table[stack[-1].val] > hash_table[node.val]:
                        u = stack.pop()
                    u.left = node
                stack.append(node)

        return head
