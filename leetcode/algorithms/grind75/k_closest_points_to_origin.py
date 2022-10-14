
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heap
        n = len(points)
        
        # Heap by default is min
        heap = [(points[i][0]*points[i][0] + points[i][1]*points[i][1], i) for i in range(n)]
        
        heapq.heapify(heap)
        
        output = []
        
        for i in range(k):
            output.append(points[heapq.heappop(heap)[1]])
        return output