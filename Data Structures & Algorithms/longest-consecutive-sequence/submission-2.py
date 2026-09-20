class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_sequence = 0

        for num in nums : 
            counter = 0
            current = num
            while current in nums :
                counter +=1 
                current += 1

            max_sequence = max(max_sequence,counter)

        return max_sequence

