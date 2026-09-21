class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right :

            r = (left + right) // 2
            if nums[r] == target:
                return r
            elif target > nums[r]:
                left = r+1
            else:
                right = r - 1

        return -1
          

        