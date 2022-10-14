"""
Implement DFS with stack and recursion
"""

a = [[0, 1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10 ,11],
     [12, 13, 14, 15, 16, 17]]

visited = [[False for _ in range(6)] for _ in range(3)]

def dfs_stack():
    """Because we maintain a stack, we can mark a node as visited as neighbor, to reduce number of functions being called"""
    visited[0][0] = True
    stack = [(0, 0)]
    while len(stack) > 0:
        i, j = stack.pop()
        neighbors = [(i + 1, j),
                     (i, j + 1),
                     (i - 1, j),
                     (i, j - 1)]
        for neighbor in neighbors:
            nei_i, nei_j = neighbor[0], neighbor[1]
            if nei_i >= 0 and nei_i < len(a) and nei_j >= 0 and nei_j < len(a[0]) and not visited[nei_i][nei_j]:
                stack.append((nei_i, nei_j))
                visited[nei_i][nei_j] = True
        print(a[i][j])

def dfs_recur(i: int, j: int) -> None:
    """No stack maintained, higher number of functions being called

    Args:
        i (int): _description_
        j (int): _description_
    """
    print(a[i][j])
    visited[i][j] = True
    neighbors = [(i + 1, j),
                 (i, j + 1),
                 (i - 1, j),
                (i, j - 1)]
    for neighbor in neighbors:
        nei_i, nei_j = neighbor[0], neighbor[1]
        if nei_i >= 0 and nei_i < len(a) and nei_j >= 0 and nei_j < len(a[0]) and not visited[nei_i][nei_j]:
            dfs_recur(nei_i, nei_j)
        

# dfs_stack()
dfs_recur(0, 0)