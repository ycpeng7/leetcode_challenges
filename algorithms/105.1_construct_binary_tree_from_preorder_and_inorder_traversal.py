#-------------------------------------------------------------------------------
#    Construct Binary Tree from Preorder and Inorder Traversal
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/Construct Binary Tree from Preorder and Inorder Traversal/
# Completed 11/24/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Recursion to build tree
2. First element of preorder is head
3. Check index of head in preorder 
4. If index > 0, means there's left child, build left
5. If index < n - 1, means there's right child, build right
"""


#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        head = TreeNode(val=preorder[0])
        head_index = inorder.index(preorder[0])
        preorder.pop(0)
        if head_index > 0:
            head.left = self.buildTree(preorder, inorder[:head_index])
        if head_index < len(inorder) - 1:
            head.right = self.buildTree(preorder, inorder[head_index + 1:])
        return head

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    
   

if __name__ == '__main__':
    unittest.main()     