#-------------------------------------------------------------------------------
#    Flatten Binary Tree to Linked List
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Completed 11/26/20
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Recursion
2. temp = root.right
3. root.right = flatten(root.left)
4. Find left leaf
5. Left leaf.right = flatten(temp)
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
    def find_leaf(self, root):
        while root.right is not None:
            root = root.right
        return root
    
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None
        temp = root.right
        root.right = self.flatten(root.left)
        root.left = None
        leaf = self.find_leaf(root)
        leaf.right = self.flatten(temp)
        return root
        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    
   

if __name__ == '__main__':
    unittest.main()     