#-------------------------------------------------------------------------------
#    Implementation of AVL Tree
#-------------------------------------------------------------------------------

class Node:
    def __init__(self, left=None, right=None, val):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1
        # Balance factor to determine whether rotation is needed: rightHeight - leftHeight
        self.bf = 0

class AVLTree:
    def __init__(self):
        self.root = None
        self.numofNodes = 0
    
    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height
    def size(self):
        return self.numofNodes
    
    def isEmpty(self):
        return self.size == 0
    
    def contains(self, val):
        return self._contains(self.root, val)

    def _contains(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif node.val < val:
            return self._contains(node.left, val)
        else:
            return self._contains(node.right, val)
        
    def add(self, val):
        if not self.contains(val):
            self.root = self._add(self.root, val)
            self.numofNodes += 1
    
    def _add(self, node, val):
        if node is None:
            node = Node(val)
        elif node.val < val:
            node.left = self._add(node.left, val)
        elif node.val > val:
            node.right = self._add(node.right, val)
        self._update(node)
        return self._balance(node)
    
    def remove(self, val):
        if self.contains(val):
            self.root = self._remove(val, self.root)
            self.numofNodes -= 1

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
        self._update(cur_node)
        return self._balance(cur_node)
    
    def _update(self, node):
        leftHeight = node.left.height if node.left is None else 0
        rightHeight = node.right.height if node.right is None else 0
        node.height = max(leftHeight, rightHeight) + 1
        node.bf = rightHeight - leftHeight

    def _balance(self, node):
        # Left heavy tree
        if node.bf == -2:
            # left-left
            if node.left.bf < 0:
                return self._leftleft(node)
            # left-right
            else:
                return self._leftright(node)
        # Right heavy tree
        elif node.bf == 2:
            # right-right
            if node.right.bf > 0:
                return self._rightright(node)
            # right-left
            else:
                return self.rightleft(node)
        return node
    
    def _leftleft(self, node):
        return self.rightrotation(node)

    def _leftright(self, node):
        node.left = self._leftRotation(node.left)
        return self._leftleft(node)

    def _rightright(self, node):
        return self._leftRotation(node)

    def _rightleft(self, node):
        node.right = self._rightRotation(node.right)
        return self._rightright(node)
    
    def _leftRotation(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self._update(node)
        self._update(newParent)
        return newParent
    
    def _rightRotation(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        self._update(node)
        self._update(newParent)
        return newParent
    


