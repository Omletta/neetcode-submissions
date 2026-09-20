import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        copy_list = nums.copy()
        product = int(math.prod(nums))

        for num in copy_list:
            mult = 1
            for j in nums :
                if j != num:


                    mult = mult * j

            output.append(mult)

        return output



        
    