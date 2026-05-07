class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod, rprod = [1], [1]
	
        for i in range(len(nums)):
            lprod = lprod + [lprod[-1]*nums[i]]
            rprod = [rprod[0]*nums[~i]] + rprod
            
        return [lprod[i] * rprod[i+1] for i in range(len(nums))]