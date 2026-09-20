import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        copy_list = nums.copy()
        

        for i in range(len(copy_list)):
            mult = 1
            for j in range(len(nums)) :
                if j != i:

                    mult = mult * nums[j]

            output.append(mult)

        return output



        
    