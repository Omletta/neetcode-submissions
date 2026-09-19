class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_length = 0

        for i in range(len(nums)) :
            counter = 1
            current_next= nums[i]+1
            while current_next in nums :
                counter +=1
                current_next +=1

            
            max_length = max(counter,max_length)

        return max_length