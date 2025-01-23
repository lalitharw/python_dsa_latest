class MinStack:
    def __init__(self):
        self.arr = []

        # we will use this to only store minimum element in an array
        self.secondArr = []

    def push(self, val:int)->None:
        self.arr.append(val)

        if(len(self.secondArr) == 0):
            self.secondArr.append(val)

        if(self.secondArr[-1] > val):
            self.secondArr.append(val)

    def pop(self)->None:
        popped = self.arr.pop()

        if(popped == self.secondArr[-1]):
            self.secondArr.pop()

        

    def top(self) -> int:
        return self.arr[-1]
    
    def getMin(self) -> int:
        return self.secondArr[-1]
    
minStack =  MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() # return 0
minStack.pop()
minStack.top()    # return 2
print(minStack.getMin()) # return 1
