class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        # Simultaneous left and right passes
        left_product = 1
        right_product = 1
        
        for i in range(n):
            # Left pass: i goes 0 → n-1
            left[i], right[~i] = left_product, right_product

            left_product *= nums[i]
            right_product *= nums[~i]
        
        # Combine step
        return [l * r for l, r in zip(left, right)]