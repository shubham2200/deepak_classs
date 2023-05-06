class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        value = 0
        Result = 0
        for i in range(len(gain)):
            value = gain[i] + value
            Result = max(value, Result)  
            print(Result,'ascxsc')

        return Result
