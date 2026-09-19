class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            j= i+1 
            while j<len(temperatures) and temperatures[j] <=temperatures[i]:
                j+=1
            
            

            if j >=len(temperatures):
                output.append(0)
                
            else:
                output.append(
                    j-i
                )


        
        return output
            