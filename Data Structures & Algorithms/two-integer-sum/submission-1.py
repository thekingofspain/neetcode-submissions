class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        else:
            items : dict[int, int] = {}
            
            for i, v in enumerate(nums):
            
                delta = target - v
                
                if delta in items:
                    return [items[delta], i]
                
                items[v] = i
            