def validParentheses(s):
    hashMap = {
        ")":"(",
        "]":"[",
        '}':'{'
    }

    stk = []

    # use pop() to remove from top
    # append() to add to top

    if(len(s) % 2 != 0):
        return False
    
    # looping through string
    for n in s:
        if n  not in hashMap:
            # we will add in stack
            stk.append(n)
        else:
            if len(stk) == 0:
                return False
            else:
                popped = stk.pop()

                # to get dict value by key use dict[n]
                if(popped != hashMap[n]):
                    return False
    return True

print(validParentheses("())"))