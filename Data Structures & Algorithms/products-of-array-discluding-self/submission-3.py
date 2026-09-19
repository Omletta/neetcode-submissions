class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            multiplied = 1

            for j in range(len(nums)):
                if i != j:
                    multiplied *= nums[j]

            output.append(multiplied)

        return output
