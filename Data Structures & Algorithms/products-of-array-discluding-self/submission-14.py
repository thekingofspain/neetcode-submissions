class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max = 1
        zc = 0 
        length = len(nums)
        r = range(len(nums))
        fz = -1

        for i in r:
            if nums[i] == 0:
                if fz == -1:
                    fz = i
                zc += 1
            else:
                max *= nums[i]

        result: list[int] = [0] * length

        if zc > 1:
            return result;
        
        if fz != -1:
            result[fz] = max
            return result;

        for i in r:
            result[i] = max // nums[i]    
            
        return result
