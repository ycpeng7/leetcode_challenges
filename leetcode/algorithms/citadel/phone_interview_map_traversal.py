# Find whether a path exists from top left to bottom right


a = [[1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 1]]

b = [[1, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [0, 1, 0, 1, 1]]

# Use dfs
# 1. create a visited map
# 2. use dfs to traverse only if 1. a = 1 for that node, 2. it's not traversed yet
# 2. check if bottom left is visited


def find_path(a) -> bool:
    rows = len(a)
    cols = len(a[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(i, j):
        if a[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            if i > 0:
                dfs(i - 1, j)
            if j > 0:
                dfs(i, j - 1)
            if i < rows - 1:
                dfs(i + 1, j)
            if j < cols - 1:
                dfs(i, j + 1)

    dfs(0, 0)

    return visited[rows-1][cols-1] == 1


    

# bfs

def find_path_bfs(a) -> bool:
    rows = len(a)
    cols = len(a[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    if a[0][0] == 0:
        return False

    queue = []    
    queue.append([0, 0])
    while len(queue) > 0:
        temp = queue.pop(0)
        i, j = temp[0], temp[1]
        if visited[i][j] == 0 and a[i][j] == 1:
            visited[i][j] = 1
            if i > 0:
                queue.append([i - 1, j])
            if j > 0:
                queue.append([i, j - 1])
            if i < rows - 1:
                queue.append([i + 1, j])
            if j < cols - 1:
                queue.append([i, j + 1])

    return visited[rows-1][cols-1] == 1



assert find_path(a) == True
assert find_path(b) == False

assert find_path_bfs(a) == True
assert find_path_bfs(b) == False