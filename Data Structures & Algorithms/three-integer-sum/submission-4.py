class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range (j+1, len(nums)):

                    if nums[i] == nums[j] == nums[k] ==0 :
                        output = [[nums[i],nums[j],nums[j+1]]]
                    elif nums[i] + nums[j] + nums[k] == 0 :
                        list = sorted([nums[i],nums[j],nums[k]])
                        if list not in output:
                            output.append(list)
                        
                    
        return output
        