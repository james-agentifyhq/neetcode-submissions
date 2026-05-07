class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in sums:
                return [sums[rem], i]
            sums[nums[i]] = i
        
        return False 