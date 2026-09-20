class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0

        for i in range(len(heights)-1): 
            for j in range(i+1,len(heights)):
                current_area = 0

                lowest_bar = min(heights[i],heights[j])

                current_area = lowest_bar * (j-i)
                
                max_container = max(max_container, current_area)

        
        return max_container