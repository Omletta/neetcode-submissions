class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setted_list = set()
        for i in range(0,len(nums)):
            if nums[i] not in setted_list:
                setted_list.add(nums[i])

            
        if len(setted_list) == len(nums):
            return False
        else:
            return True
        
        