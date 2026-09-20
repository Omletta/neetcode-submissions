class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_sequence = 0

        for num in nums : 
            counter = 1
            while num + 1 in nums :
                counter +=1 
                num = num + 1

            max_sequence = max(max_sequence,counter)

        return max_sequence

