class RemoveKDigit:
    # https://algo.monster/liteproblems/402

    '''
    basically all we have to do it
    first we checked if stack is empty
    if it is empty append in stack
    if not check if top most element in stack[-1]  is greater than the current element
    if yes pop() the element from stack and append the current element smaller element in it.
    '''

    def __init__(self,arr,digit):
        self.digit = digit
        self.arr = arr

    def removeDigits(self):
        stk = []

        digitsRemoved = 0

        for a in self.arr:
            if(digitsRemoved > self.digit):
                break

            if(stk):
                if(stk[-1] > a):
                    digitsRemoved += 1
                    stk.pop()
                    stk.append(a)
                else:
                    stk.append(a)
            else:
                stk.append(a)

        return ("".join(stk).lstrip("0"))



    


k = RemoveKDigit("1432219",3)

print(k.removeDigits())
