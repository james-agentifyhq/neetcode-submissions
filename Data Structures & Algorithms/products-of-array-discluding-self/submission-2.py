from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] + list(accumulate(nums[:-1], mul))
        
        suffix_input = nums[1:][::-1]
        
        suffix_accumulated = list(accumulate(suffix_input, mul))
        
        suffix = suffix_accumulated[::-1] + [1]
        
        return [p * s for p, s in zip(prefix, suffix)]