class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            r = (left + right) // 2

            if nums[r] > nums[right]:
                left = r + 1
            else:
                right = r

        return nums[left]