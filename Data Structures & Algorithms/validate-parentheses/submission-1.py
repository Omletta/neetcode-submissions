class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s :
            if c in '{[(':
                stack.append(c)
            while stack : 
                if c != stack[-1]:
                    return False
                print(stack)
                stack.remove(stack[-1])
                print(stack)
            

                


        return True
