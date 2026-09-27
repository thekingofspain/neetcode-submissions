class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def itemCount(n: int) -> int:
            return items[n]

        items : dict[int, int] = {} # value, count 
        
        for n in nums:
            items[n] = items.get(n, 0) + 1

        return sorted(items.keys(), key = itemCount, reverse = True)[:k]

        