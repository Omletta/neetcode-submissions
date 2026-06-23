class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
 
        while left <= right:
                
                r = (left+right)//2
                if target< nums[r]:
                    right = r-1
                elif target > nums[r]:
                    left = r+1
                elif nums[r] == target  : 
                    return r
        return -1

        