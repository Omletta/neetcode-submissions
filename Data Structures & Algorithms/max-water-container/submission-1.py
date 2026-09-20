class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area= 0

        left = 0

        right = len(heights) - 1
        print(right)
        

        while left < right: 
            area =(right - left ) * min(heights[left],heights[right])
            if heights[left ] <= heights[right] : 
                left = left + 1 

            else :
                right = right -1 

            max_area = max(area,max_area)

            
        return max_area



            


        ###for i in range(len(heights)-1): 
         ###   for j in range(i+1,len(heights)):
           ###     current_area = 0

           ###     lowest_bar = min(heights[i],heights[j])

           ###     current_area = lowest_bar * (j-i)
                
           ###     max_container = max(max_container, current_area)

        
        return max_container