class ReversePolish:
    def evalPRN(self,tokens) -> int:
        stk = []

        for t in tokens:

            # if operater comes
            if t in "+-*/":
                b,a = stk.pop(), stk.pop()

                if(t == "+"):
                    stk.append(a+b)
                elif(t == "-"):
                    stk.append(a-b)
                elif(t == "*"):
                    stk.append(a*b)

                else:
                    stk.append(a/b)

            else:
                # if operand comes
                 
                # dont forget it to convert into int
                stk.append(int(t))
        
        return stk[-1]
    

rpn  = ReversePolish()
print(rpn.evalPRN(["1","2","+","3","*","4","-"]))

                
            

   