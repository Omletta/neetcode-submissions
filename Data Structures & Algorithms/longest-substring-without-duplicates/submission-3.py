class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sequence = 0

        
        left = 0
        right = 0
        seen = set()

        if len(s) == 0:
            return 1

        for right in range(len(s)):
            
            while s[right] in seen :
                seen.remove(s[left])
                left +=1

            seen.add(s[right])
            max_sequence = max(max_sequence , right - left + 1)
            
        return max_sequence

