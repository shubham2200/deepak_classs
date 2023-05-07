class Solution:
    def maximumDifference(self, n: List[int]) -> int:
        min_value = 1e9
        max_value = 0 
        
        for i in range(len(n)):
            min_value = min(min_value, n[i])
            max_value = max(max_value , n[i] - min_value)
        print(max_value)
        if max_value == 0:
            return -1
        return max_value
