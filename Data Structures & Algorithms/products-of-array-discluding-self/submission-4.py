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

        result: list[int] = []    

        if zc > 1:
            return [0] * len(nums)
        
        for n in nums:
            
            value: int = 0

            if n == 0:
                value = max
            elif zc == 0:
                value = max // n    
            
            result.append(value)

        return result
