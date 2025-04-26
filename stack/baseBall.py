//test

class BaseBall:
    def __init__(self,arr):
        self.arr = arr

    def sum(self) -> int:

        stk = []
        # if c comes remove it from stack
        # if d comes take top 2 elements, double it and add it back
        for s in self.arr:
            print(s)
            if(s == 'C'):
                stk.pop()

            elif(s == "D"):
                a = stk[-1]
                double  = a*2
                stk.append(double)

            elif(s == "+"):
                b,a = stk[-1], stk[-2]
                sum = a + b
                stk.append(sum)
            else:
                stk.append(int(s))

        plus = 0
        for stack in stk:
            plus += stack
        return plus

            

base = BaseBall(["5","-2","4","C","D","9","+","+"])


print(base.sum())

