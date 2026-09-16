class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        

        s2 = ''.join(c for c in s if c.isalpha()).lower()
        right = len(s2)-1
        print(s2)
        while left < right:
            if s2[left] != s2[right]:
                return False
            left +=1 
            right -=1

        return True
