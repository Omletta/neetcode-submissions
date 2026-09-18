class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s :
            if c in '{[(':
                stack.append(c)
            if stack and c!= stack[-1] : 
                return False
                print(stack)
            if stack :
                stack.remove(stack[-1])
            else:
                return True
            print(stack)
            

                


        return True
