class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens :
            
            if token in '+-*/':
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    res = b+a

                elif token == '-':
                    res= a - b
                elif token =='*':
                    res = a*b

                elif token =='/':
                    res = a/b

                stack.append(res)
            else:
                stack.append(token)
            
        return res
            
                
