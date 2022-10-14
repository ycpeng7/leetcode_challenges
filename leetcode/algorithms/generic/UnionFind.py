#-------------------------------------------------------------------------------
#    Implementation of Union Find using list
#-------------------------------------------------------------------------------

class UnionFind:
    def __init__(self, size: int = 1):
        self.size = size
        # parent of each component, if parent[i] == i, then i is root node
        self.parent = [i for i in range(size)]
        # Size of each component
        self.sz = [1 for i in range(size)]
        self.numofSet = size

    # Find which set the node belongs to (find the parent), takes amortized constant time (with path compression)
    def find(self, val: int):
        if val >= self.size or val < 0:
            print("Invalid node")
            return
        root = val
        # Find root
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression to point all nodes directly to root
        while self.parent[val] != val:
            par = self.parent[val]
            # Point to root
            self.parent[val] = root
            val = par
        return root

    # Check if two nodes are connected
    def connected(self, p: int, q: int):
        return self.parent[p] == self.parent[q]

    # Find the size of the set p belongs to
    def componentsize(self, p: int):
        return self.sz[self.find(p)]

    def unify(self, p: int, q: int):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return
        
        # Merge smaller set to bigger one
        if self.componentsize(root1) < self.componentsize(root2):
            self.parent[root1] = root2
            self.sz[root2] += self.sz[root1]
        else:
            self.parent[root2] = root1
            self.sz[root1] += self.sz[root2]
        
        self.numofSet -= 1




