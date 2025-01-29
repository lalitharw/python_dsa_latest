def pattern(arr):
    stk  = []
    second_highest = float("inf")

    for idx in arr:

        if(idx < second_highest):
            return True

        while(stk and stk[-1] < idx):
            second_highest = stk.pop()

        stk.append(idx)

    return False


# we just have to some how find second highest number

print(pattern([3,1,4,2]))

