class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. Create an empty output list
        2. While loop, for each interval, check if start >= newInterval, if it does, this is where we should insert, do not insert yet, break
        3. Otherwise, insert the interval into output list
        4. If output list is not empty, merge the newInterval with the last one in output list
        5. Starting from the inserted interval, traverse through the remaining of uninserted intervals and merge if needed.
        
        Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in             some conditions", and typically propose an unsorted input.
        
        The standard solution has \mathcal{O}(N \log N)O(NlogN) time complexity and consists of two parts:

        Figure out how to sort the input data (\mathcal{O}(N \log N)O(NlogN) time). That could be done directly by a sorting or indirectly by a         heap usage. Typically sort is better than the heap usage because of gain in space.

        Parse the sorted input to have a solution (\mathcal{O}(N)O(N) time).
        
        """

        
        n = len(intervals)
        i = 0
        new_start = newInterval[0]
        new_end = newInterval[1]
        output_list = []
        
        
        while i < n:
            if intervals[i][0] < new_start:
                output_list.append(intervals[i])
                i += 1
            else:
                break
        
        if i > 0 and output_list[-1][1] >= new_start:
            output_list[-1][1] = max(new_end, output_list[-1][1])
        else:
            output_list.append(newInterval)
        
        j = i
        
        while j < n:
            if intervals[j][0] <= output_list[-1][1]:
                output_list[-1][1] = max(output_list[-1][1], intervals[j][1])
            else:
                output_list.append(intervals[j])
            j += 1
        
        return output_list
        
        

                        