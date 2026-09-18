class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s :
            if c in '{[(':
                stack.append(c)
            while stack : 
                if c != stack[-1]:
                    return False
                stack.remove(stack[-1])
            

                


        return True
