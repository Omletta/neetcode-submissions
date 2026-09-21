class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
            
        
        while left <  right :
            r = (left+right) // 2

            if nums[r-1] > nums[r] :
                return nums[r]
            elif nums[r-1] < nums[r]:
                left = r +1

        return nums[0]

        