class Solution:
    key: str = "ā"
    def encode(self, strs: List[str]) -> str:
        list: List[str] = []

        for s in strs:
            #list.append(str(len(s)) + self.key + s)
            list.append(s + self.key)

        return "".join(list)

    def decode(self, s: str) -> List[str]:

        return s.split(self.key)[:-1]
   