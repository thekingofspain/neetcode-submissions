class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max = 1
        length = len(nums)
        r = range(len(nums))
        fzi = -1

        result: list[int] = [0] * length

        for i in r:
            if nums[i] == 0:
                if fzi == -1:
                    fzi = i
                else:
                    return result

            else:
                max *= nums[i]

        if fzi != -1:
            result[fzi] = max
            return result

        for i in r:
            result[i] = max // nums[i]

        return result
