class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)-1):
                if nums[i] == nums[j] == nums[j+1] ==0 :
                    output = [[nums[i],nums[j],nums[j+1]]]
                elif nums[i] + nums[j] + nums[j+1] == 0 :
                    list = sorted([nums[i],nums[j],nums[j+1]])
                    if list not in output:
                        output.append(list)
                    
                    
        return output
        