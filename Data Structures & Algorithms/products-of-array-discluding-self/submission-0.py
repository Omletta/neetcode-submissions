class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_copy = nums.copy()
        output=[]

        for x in nums_copy:
            multiplied = 1
            for y in nums :
                if y != x :
                    multiplied = multiplied * y
                else : 
                    multiplied = multiplied  * 1
            x = multiplied
            output.append(x)

        print(output)

        return output 
