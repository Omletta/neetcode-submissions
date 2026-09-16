class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sequence = 0

        
        left = 0
        right = 0
        seen = []

        for i in range(0,len(s)) :
            max_sequence = max(max_sequence, right - left )
            while s[i] in seen :
                seen.remove(seen[0])
                left +=1
                
            
            seen.append(s[i])
            right +=1 
        print(max_sequence)
        return max_sequence


