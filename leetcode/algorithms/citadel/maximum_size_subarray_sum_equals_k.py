class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        1. Use a hashmap to store the prefix sum (sum(nums[0 ~ i])) and the index.
        We know that sum(nums[j ~ i]) = prefix_sum_i - prefix_sum_j
        2. If there exists an prefix_sum_j such that K = prefix_sum_i - prefix_sum_j, we know the j ~ i subarray sum is K.
        3. So, try to get {prefix_sum_i - k} and calculate subarray length if there's a match.
        4. store {prefix_sum_i: i}, if the key hasn't been seen yet. If the key is already seen, do not update,
        because we want the longest subarray.       
        """
        
        longest = 0
        
        prefix_sum = {}
        sum_so_far = 0
        
        for i in range(len(nums)):
            sum_so_far += nums[i]
            if sum_so_far == k:
                longest = i + 1    
            elif prefix_sum.get(sum_so_far - k) is not None:
                j = prefix_sum.get(sum_so_far - k)
                longest = max(longest, i - j)
            if prefix_sum.get(sum_so_far) is None:
                prefix_sum[sum_so_far] = i
        return longest