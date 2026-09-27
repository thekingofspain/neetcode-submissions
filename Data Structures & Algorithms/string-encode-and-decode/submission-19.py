class Solution:
    def encode(self, strs: List[str]) -> str:
        list: List[str] = []

        for s in strs:
            list.append(str(len(s)) + "ā" + s)

        return "".join(list)

    def decode(self, s: str) -> List[str]:
        items: List[str] = []

        i = 0
        first_digit = 0
        s_size = len(s)
        w_size = 0

        while i < s_size:
            c = s[i]

            if c == "ā":
                w_size = int(s[first_digit:i])
                first_digit = i + 1 + w_size 
                items.append(s[i + 1 : first_digit]) # goofy python, upto next digit
                i = first_digit + 1

            else:
                i += 1

        return items


# 0123456789012
# 5āHello5āWord
