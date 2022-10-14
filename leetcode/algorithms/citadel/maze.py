# Find whether a path exists from top left to bottom right


a = [[1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 1]]

a2 = [[1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0]]

b = [[1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [0, 1, 0, 1, 1]]

# and also the shortest distance and corresponding path


def path_exists(a) -> bool:
    """
    Use dfs to check if path exists
    """

    visited = [[False for _ in range(len(a[0]))] for _ in range(len(a))]
    
    def dfs(i, j):
        in_boundary = i >= 0 and i < len(a) and j >= 0 and j < len(a[0])
        if not in_boundary or a[i][j] == 0 or visited[i][j] or visited[len(a) - 1][len(a[0]) - 1]:
            return
        
        visited[i][j] = True


        neighbors = [[i + 1, j],
                     [i, j + 1],
                     [i - 1, j],
                     [i, j - 1]]
        for neighbor in neighbors:
            dfs(neighbor[0], neighbor[1])
    
    dfs(0, 0)

    return visited[len(a) - 1][len(a[0]) - 1]


def shortest_path(a):
    """
    Use BFS.

    1. Initiate a distance matrix with max int.
    2. Start from origin, if neighbor distance is larger than distance + 1, replace it (this also marks it visited, since for BFS, the first time a node is visited,
    it's guaranteed to have shortest distance).
    3. Store the previous path in the queue,  if a node distance has been updated, add it to the end of the popped path and append it the queue.
    4. If visited the destination, break the loop.
    """

    m = len(a)
    n = len(a[0])

    distance = [[float("inf") for _ in range(n)] for _ in range(n)]

    distance[0][0] = 0

    queue = [[[0,0]]]

    while(len(queue) > 0):
        path_to_node = queue.pop(0)
        i, j = path_to_node[-1]
        
        neighbors = [[i + 1, j],
                     [i, j + 1],
                     [i - 1, j],
                     [i, j - 1]]
        
        for neighbor in neighbors:
            nei_i, nei_j = neighbor
            in_boundary = nei_i >= 0 and nei_i < m and nei_j >= 0 and nei_j < n
            if in_boundary and a[nei_i][nei_j] == 1 and distance[nei_i][nei_j] > distance[i][j] + 1:
                distance[nei_i][nei_j] = distance[i][j] + 1
                queue.append(path_to_node + ([[nei_i, nei_j]]))
                if nei_i == m - 1 and nei_j == n - 1:
                    print("DISTANCE: ", distance[m-1][n-1], "PATH: ", queue[-1])




assert path_exists(a) == True
assert path_exists(a2) == False
    

shortest_path(a)
shortest_path(b)