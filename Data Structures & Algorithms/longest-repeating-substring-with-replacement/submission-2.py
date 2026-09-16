class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
       str_char = set(s)

       window = 0
       frequency = {}

       for c in str_char:
        left = 0


        right = 1
        frequency[c]=s.count(c)

        while left <= right and right <= len(s) :
            if (right-left+1) - frequency[c] <= k:
                    window =max(window,right-left+1)
                    right +=1
            else:
                left +=1


       
        return window

