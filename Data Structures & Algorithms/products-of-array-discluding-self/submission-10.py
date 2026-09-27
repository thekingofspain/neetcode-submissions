class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max = 1
        zc = 0 

        if len(nums) == 1:
            return nums

        for n in nums:
            if n == 0:
                zc += 1
            else:
                max *= n

        result: list[int] = [0] * len(nums)
        value = 0

        if zc > 1:
            return result;
            
        for i in range(len(nums)):
            value = 0
            
            if nums[i] == 0:
                value = max
            elif zc == 0:
                value = max // nums[i]    
            
            result[i] = value

        return result
