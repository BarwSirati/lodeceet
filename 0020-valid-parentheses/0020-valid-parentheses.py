class Stack:
    def __init__(self):
        self.s = []
    def add(self,value:str):
        self.s.append(value)
    def pop(self):
        if self.check():
            return self.s.pop()
    def check(self):
        return len(self.s)
    def peek(self):
        if self.check():
            return self.s[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        pOpen = "({["
        pClose = ")}]"
        for i in s:
            if(i in pOpen):
                stack.add(i)
            else:
                try:
                    if pClose.find(i) == pOpen.find(stack.peek()):
                        stack.pop()
                    else:
                        return False
                except:
                    return False
        if stack.check() == 0:
            return True
        else:
            return False

