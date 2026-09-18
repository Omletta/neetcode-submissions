class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s :
            if c in '{[(':
                stack.append(c)
            if stack and c == stack[-1] : 
                stack.remove(stack[-1])
            print(stack)
        if stack : 
            return False

        return True

            
