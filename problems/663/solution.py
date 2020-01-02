# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: 'TreeNode') -> bool:
        def helper(root: 'TreeNode') -> bool:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                root.sum = root.val
                return root.val
            left = helper(root.left)
            right = helper(root.right)
            root.sum = left + right + root.val
            return root.sum
        def search(root: 'TreeNode', num: int) -> bool:
            if root is None:
                return False
            if root.sum == num:
                return True
            return search(root.left, num) or search(root.right, num)
                
            
        helper(root)
        return search(root.left, root.sum / 2) or search(root.right, root.sum / 2)