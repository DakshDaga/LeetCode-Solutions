# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def subTree(node):
            count, node_sum = 1, node.val
            if node.left:
                subCount, sub_sum = subTree(node.left)
                count += subCount
                node_sum += sub_sum
            if node.right:
                subCount, sub_sum = subTree(node.right)
                count += subCount
                node_sum += sub_sum
            
            if node_sum // count == node.val: self.ans += 1
            return count, node_sum

        subTree(root)
        return self.ans