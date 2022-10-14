class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        """
        BFS starting from 0 nodes
        
        1. For each 0 element in matrix, set dist = 0, otherwise MAX
        2. push every 0 element in a queue, this queue is for BFS on 0 nodes
        3. Running BFS on 0 nodes instead of on 1s because the former can set distance for all its 1 neighbors,
        but latter would only get the distance for itself for 1 BFS run, which is worse than brute force.
        4. Run BFS on the queue, if the calculated distance for that neighbor (self dist + 1) is smaller than current one,
        set it as that, and push that neighbor to the queue. Since now that neighbor is guaranteed to have minimum distance (all the 0 nodes
        preceed 1s in the queue).
        """
        
        m = len(mat)
        n = len(mat[0])
        
        distance = [[0 for _ in range(n)] for _ in range(m)]
        queue = []
        
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append([i, j])
                else:
                    distance[i][j] = float('inf')
        
        
        while len(queue) > 0:
            i, j = queue.pop(0)
            neighbors = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
            
            for neighbor in neighbors:
                i_nei, j_nei = neighbor[0], neighbor[1]
                if i_nei >= 0 and i_nei < m and j_nei >= 0 and j_nei < n:
                    if distance[i_nei][j_nei] > distance[i][j] + 1:
                        distance[i_nei][j_nei] = distance[i][j] + 1
                        queue.append([i_nei, j_nei])
        
        return distance