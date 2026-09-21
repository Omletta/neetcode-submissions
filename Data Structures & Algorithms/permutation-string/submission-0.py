class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = len(s1)

        while right <= len(s2):
            
            print(set(s2[left:right]),set(s1))
            if set(s2[left:right]) == set(s1):
                return True
            

           
        
            left += 1
            right += 1

        return False