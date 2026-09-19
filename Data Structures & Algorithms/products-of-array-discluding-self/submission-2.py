class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        list_copy = nums.copy()
        output = []

        if len(nums) == 2:
            return [0,0]
        for x in list_copy:
            
            multiplied = 1
        
            for y in nums :
                if y != x  :
                    multiplied = multiplied * y
                elif y == 0 and y!= x :
                    multiplied = 0

                

            output.append(multiplied)

        print(output)

        return output 
