class Stack:
    def __init__(self,length):
        self._data = []
        self.length = length

    def len(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def is_full(self):
        return len(self._data) == self.length
    
    def push(self,e):
        if(self.is_full()):
            return "Stack is Full"
        self._data.append(e)
        self

    def pop(self):
        if(self.is_empty()):
            return("Stack is Empty")
        return self._data.pop()
    
s = Stack(2)

print(s.push(1))
print(s.len())
