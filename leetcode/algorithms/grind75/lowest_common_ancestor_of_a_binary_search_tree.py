# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
       # Recursion
       # 1. If p and q are both larger than cur, call recursion on right
       # 2. If p and q are both smaller than cur, call recursion on left
       # 3. Else, we know p and q are at different side, hence the LCA
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p , q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p , q)
        else:
            return root