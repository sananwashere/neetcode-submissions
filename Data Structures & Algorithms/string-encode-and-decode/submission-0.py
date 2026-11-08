class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []
        for i in range(len(strs)):
            new_strs.append(str(len(strs[i])) + '#' + strs[i])

        return "".join(new_strs)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[ j + 1 : j + 1 + length])
            i = j + length + 1
        return res



# 1 -> find length of string, add length then # e.g. hi -> 2#hi
# loop through strs, add value to variable 
