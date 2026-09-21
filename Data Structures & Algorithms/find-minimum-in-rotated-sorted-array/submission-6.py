class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
            
        
        while left <  right :
            r = (left+right) // 2

            if r != 0 and nums[r-1] > nums[r] :
                return nums[r]
            elif r == 0 and nums[r-1] > nums[r] : 
                return nums[r-1]
            elif r!=0 and nums[r-1] < nums[r]:
                left = r +1
            

        return nums[0]

        