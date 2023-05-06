1446. Consecutive Characters 
 ct = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                ct += 1
            else:
                ct = 1
            res = max(res, ct)
        return 1 if len(s) == 1 else res
        # TC O(n)
        # SC O(1)
