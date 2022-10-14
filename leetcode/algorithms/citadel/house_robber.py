class Solution:
    def max_money(self, i: int) -> int:
        if i >= len(self.nums):
            return 0
        elif self.memo[i] is not None:
            return self.memo[i]
        else:
            self.memo[i] = max(self.nums[i] + self.max_money(i + 2), self.max_money(i + 1))
            return self.memo[i]
        
    
    def rob(self, nums: List[int]) -> int:
        """
        For each index, max[i] = max(nums[i] + max(i + 2), max[i + 1])
        """
        self.nums = nums
        self.memo = [None] * len(nums)
        
        return self.max_money(0)