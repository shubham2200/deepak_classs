class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        res = 0 
        for i in range( len(nums)):
            if nums[i] == 1:
                ct += 1
            else:
                ct = 0
            res = max(ct, res)
        print(res)
        return res
        # TC = o(n)
        # SC = o(1)
