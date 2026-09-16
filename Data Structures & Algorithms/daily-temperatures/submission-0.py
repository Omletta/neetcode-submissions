class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

    
        for i in range(0,len(temperatures)) :
            left = i 
            right = i+1

            while right <len(temperatures) and temperatures[right] <= temperatures [left]:

                right += 1
            if right == len(temperatures)  :
                result.append(0)
            else:

                result.append(right - left)

            
        return result