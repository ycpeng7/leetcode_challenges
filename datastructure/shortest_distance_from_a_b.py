from math import dist


a = [[1, 0, 1, 1, 1],
     [1, 1, 1, 0, 1],
     [0, 1, 1, 1, 1],
     [0, 0, 0, 0, 1]]
# shortest path = 7

"""
Find shortest path and distance from top left to bottom right

1. Initiate distance matrix at Inf (can be used as visited too).
2. Use BFS to start from top left, neighbor's distance = cur distance + 1. Since it's guaranteed the first time a node is visited, it's shortest path to it with BFS.
3. Store the path to the node in the queue instead. If neighbor distance is larger than cur distance + 1, append the path + neighbor to queue
4. Return when neighbor is end node.
"""

m = len(a)
n = len(a[0])

distance = [[float('Inf') for _ in range(n)] for _ in range(m)]

def bfs(queue, i, j):
    
    while len(queue) > 0:
        print("Q: ", queue)
        path = queue.pop(0)
        i, j = path[-1]
        cur_distance = distance[i][j]
        neighbors = [[i + 1, j],
                     [i, j + 1],
                     [i - 1, j],
                     [i, j - 1]]
        for neighbor in neighbors:
            nei_i, nei_j = neighbor[0], neighbor[1]
            nei_distance = distance[nei_i][nei_j]
            in_boundary = nei_i >= 0 and nei_i < m and nei_j >= 0 and nei_j < n
            if in_boundary and a[nei_i][nei_j] == 1 and nei_distance > cur_distance + 1:
                 new_path = path + [[nei_i, nei_j]]
                 print("PATH: ", new_path)
                 queue.append(new_path)
                 distance[nei_i][nei_j] = cur_distance + 1
                 if nei_i == m-1 and nei_j == n-1:
                     return

def find_path():
    queue = []
    queue.append([[0, 0]])
    distance[0][0] = 0
    bfs(queue, 0, 0)
    print(queue[-1])
    print(distance[m-1][n-1])

find_path()