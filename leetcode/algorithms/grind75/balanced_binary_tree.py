# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        """
        Top-down recursion
        
        Two conditions for each node:
        
        1. left and right tree are both balanced
        2. Self is also balanced
        
        This has redundant height calculation, so bottom up is better.
        """
        
        
#         def height(node):
#             if node is None:
#                 return 0
#             else:
#                 return 1 + max(height(node.left), height(node.right))
            
#         if root is None:
#             return True
#         elif not (self.isBalanced(root.left)) or not (self.isBalanced(root.right)):
#             return False
#         else:
#             left_height = height(root.left)
#             right_height = height(root.right)
#             return not (left_height > right_height + 1) and not (right_height > left_height + 1)
        
        
        """
        Bottom-up recursion:
        
        When calculating height, also check height difference. Use a global variable, can skip calculation when
        we know at least a subtree is imbalanced.
        
        """
        
        self.balanced = True
        
        def height(node):
            if node is None or not self.balanced:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            if (left_height > (right_height + 1)) or (right_height > (left_height + 1)):
                self.balanced = False
                return 0

            return 1 + max(left_height, right_height)
        
        self_height = height(root)
        
        return self.balanced == True