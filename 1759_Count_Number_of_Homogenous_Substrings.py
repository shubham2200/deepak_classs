class Solution:
    def countHomogenous(self, s: str) -> int:
        final_char_num = 0
        add = 0
        mode  = 1e9 + 7
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                add+=1
            else:
                add = 1
            final_char_num = (final_char_num + add) % mode
        print(add)
        return int(final_char_num)
        # type casting 
        # TC = o(n)
        # SC = o(1)
