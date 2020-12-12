#-------------------------------------------------------------------------------
#    Implementation of Binary Search Tree
#-------------------------------------------------------------------------------

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.nodeCount
    
    # Public method for adding Node
    def add(self, val):
        if not self.contains(val):
            self.root = self._add(val, self.root)
            self.nodeCount += 1
    
    def _add(self, val, cur_node):
        if cur_node is None:
            return Node(val)
        if val < cur_node.val:
            cur_node.left = self._add(val, cur_node.left)
        else:
            cur_node.right = self._add(val, cur_node.right)
        return cur_node

    def remove(self, val):
        if self.contains(val):
            self.root = self._remove(val, self.root)
            self.nodeCount -= 1

    def _digright(self, node):
        while node.right is not None:
            node = node.right
        return node

    def _remove(self, val, cur_node):
        if val < cur_node.val:
            cur_node.left = self._remove(val, cur_node.left)
        else:
            cur_node.right = self._remove(val, cur_node.right)
        
        if val == cur_node.val:
            if cur_node.left is None and cur_node.right is None:
                del cur_node
                return None
            elif cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left
            # If neither of the children is None, replace the current node with largest of the left subtree
            else:
                largest = self._digright(cur_node.left)
                largest.val, cur_node.val = cur_node.val, largest.val
                cur_node.left = self._remove(largest.val, cur_node)
        return cur_node

    def height(self):
        return self._height(self.root)
    
    def _height(self, node: Node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1
    
    def contains(self, val):
        return self._search(val, self.root)

    def _search(self, val, cur_node):
        if cur_node.val == val:
            return True
        if cur_node is None:
            return False
        if val < cur_node.val:
            return self._search(val, cur_node.left)
        else:
            return self._search(val, cur_node.right) 

