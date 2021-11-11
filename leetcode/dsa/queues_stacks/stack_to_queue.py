class MyStack:
    
    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.insert(0,x)
        

    def pop(self) -> int:
        ele = self.stack.pop(0)
        return ele

    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        
