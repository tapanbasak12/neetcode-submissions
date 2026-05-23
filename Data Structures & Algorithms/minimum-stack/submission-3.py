class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.g_min=float(('inf'))
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.g_min:
            self.g_min=val
            self.min_stack.append(self.g_min)
        

    def pop(self) -> None:
        x= self.stack.pop()
        if x== self.min_stack[-1]:
            self.min_stack.pop()
            self.g_min = self.min_stack[-1] if self.min_stack else float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
