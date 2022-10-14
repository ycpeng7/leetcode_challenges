class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        lis = []
        for i in range(len(nums)):
            if map.get(nums[i]) == None:
                map[target-nums[i]] = i
            else:
                return [map.get(nums[i]), i]
        return lis


assert Solution.twoSum([1,2], 2) == [1]