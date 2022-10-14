class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a possibility.
        We only keep the num if the num doesn't make our current sum negative, that is, num > sum + num, so current sum is
        max(num, curSum + num)
        """

        maxSum = curSum = nums[0]
        
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)
        return maxSum