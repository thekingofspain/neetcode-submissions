class Solution:

    def counterIndex(self, c: str) -> int:
        return ord(c) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = [0] * 26

        for i in range(len(s)):
            counter[self.counterIndex(s[i])] += 1
            counter[self.counterIndex(t[i])] -= 1

        return all(x == 0 for x in counter)

    