class MinStack:
    """
    def __init__(self):
        self.stack_mini = [np.inf]
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack and self.stack[-1] <= self.stack_mini[-1]:
            self.stack_mini.append(self.stack[-1])
        
    def pop(self) -> None:
        if self.stack_mini[-1] == self.stack[-1]:
            self.stack_mini.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mini[-1]"""

    def __init__(self):
        self.stack =  []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
