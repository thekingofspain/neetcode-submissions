class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        if len(nums) == 0:
            return False

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        
        