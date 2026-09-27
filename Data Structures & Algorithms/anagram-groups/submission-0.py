class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result : dict[str, List[str]] = {}

        for c in strs:
            key = "".join(sorted(c))
            
            if key in result:
                result[key].append(c)
            else:
                result[key] = [c]

        return list(result.values())
        