class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        
        for num in nums:
            if dict.get(num) == None:
                dict[num] = 1
            else:
                dict[num] += 1
        
        heap = []
        
        for key, val in dict.items():
            heap.append((-val, key))            
        
        heapq.heapify(heap)
        
        output = []
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
            
        return output