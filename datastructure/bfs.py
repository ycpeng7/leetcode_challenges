"""
Implement BFS with loop and recursion
"""

a = [[0, 1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10 ,11],
     [12, 13, 14, 15, 16, 17]]

visited = [[False for _ in range(6)] for _ in range(3)]

def bfs_loop():
    q = []
    q.append((0, 0))
    visited[0][0] = True
    while len(q) > 0:
        i, j = q.pop(0)
        neighbors = [(i + 1, j),
                     (i, j + 1),
                     (i - 1, j),
                     (i, j - 1)]
        for neighbor in neighbors:
            nei_i, nei_j = neighbor[0], neighbor[1]
            if nei_i >= 0 and nei_i < len(a) and nei_j >= 0 and nei_j < len(a[0]) and not visited[nei_i][nei_j]:
                q.append((nei_i, nei_j))
                visited[nei_i][nei_j] = True
        print(a[i][j])

def bfs_recur(q) -> None:
    if len(q) > 0:
        i, j = q.pop(0)
        neighbors = [(i + 1, j),
                     (i, j + 1),
                     (i - 1, j),
                     (i, j - 1)]
        for neighbor in neighbors:
            nei_i, nei_j = neighbor[0], neighbor[1]
            if nei_i >= 0 and nei_i < len(a) and nei_j >= 0 and nei_j < len(a[0]) and not visited[nei_i][nei_j]:
                q.append((nei_i, nei_j))
                visited[nei_i][nei_j] = True
        print(a[i][j])
        bfs_recur(q)


def bfs():
    q = []
    q.append([0, 0])
    visited[0][0] = True
    bfs_recur(q)

bfs()
# bfs_loop()