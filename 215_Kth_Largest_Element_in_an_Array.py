class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        Length = len(nums) 
        nums.sort()
        print(nums,'ascasdc')
        
        return nums[Length - k] 
