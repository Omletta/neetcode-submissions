class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s :
            if c in '{[(':
                stack.append(c)
            
                   
            if stack :
                if (stack[-1] == '{' and  c == '}') or (stack[-1] == '(' and  c == ')') or stack[-1] == '[' and  c == ']' :
                    stack.pop()
            

        if not stack :
            return True

        return False
            
            
        

            
