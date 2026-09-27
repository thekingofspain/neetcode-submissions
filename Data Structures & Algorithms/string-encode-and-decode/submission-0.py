class Solution:

    def encode(self, strs: List[str]) -> str:
        buffer = ""

        for s in strs:
            buffer += str(len(s)) + "#" + s

        return buffer

    def decode(self, s: str) -> List[str]:
        items: [str] = []

        i = 0
        fd = 0
        s_size = len(s)
        buffer = ""
        w_size = 0

        while i < s_size:
            c = s[i]
            
            if c == "#":
                w_size = int(s[fd: i])
                fd = i + 1 + w_size
                print(f"i = {i},  fd = {fd}")
                items.append(s[i + 1: fd])
                i = fd + 1
    
            else:
                i += 1

        return items
#0123456789012        
#5#Hello5#Word