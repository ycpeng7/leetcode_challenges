class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. Sort the array
        2. Traverse through each interval (i), check if the ending of the current end >= start of the next,
           if it is, set end = max(end, next_end) and traverse (j) until current end < start of the next. Then append start and end and Set i = j
        """
        
        sorted_intervals = sorted(intervals)
        
        i = 0
        
        merged_intervals = []
        
        while i < len(intervals):
            end = sorted_intervals[i][1]
            start = sorted_intervals[i][0]
            j = i + 1
            
            while j < len(intervals) and end >= sorted_intervals[j][0]:
                end = max(end, sorted_intervals[j][1])
                j += 1
            merged_intervals.append([start, end])
            i = j
        return merged_intervals
                