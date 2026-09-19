class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.prev_min_stack = []
        

    def push(self, val: int) -> None:
        if val <= self.min : 
            self.prev_min_stack.append(self.min)
            self.min = val
            
            self.stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        while self.stack[-1 ]== self.min:
            self.min = self.prev_min_stack[-1]
            self.stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
