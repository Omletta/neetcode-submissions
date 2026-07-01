class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        nums = sorted(nums)
        for i in range (0,len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1 
            right = len(nums)-1
            while left < right:

                total = nums[i] + nums[left]+ nums[right]

                if total >0:
                    right = right -1
                elif total <0:
                    left = left +1

                else : 
                    output.append([nums[i],nums[left],nums[right]])
                    right = right -1
                    left = left +1

        return output