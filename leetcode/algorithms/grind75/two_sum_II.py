class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Sorted Array.

        Two pointers
        
        1. One from start, one from end
        2. If sum larger than target, move right pointer
        3. Else, move left pointer
        
        """
        
        i, j = 0, len(numbers) - 1
        
        while j > i:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1