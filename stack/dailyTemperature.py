class DailyTemperature:

    def calculateWarmDays(self,temperature):
        stk = []
        result = [0] * len(temperature)
        for index,item in enumerate(temperature):

            # if stack have some element present and current temperature is greater than temperatuee at got at top i mean warmer
            while stk and temperature[stk[-1]] < item:

                # pop from stack and store it
                popped_index = stk.pop()

                # and then store days in result in specific index
                result[popped_index] = index - popped_index

            # if stack is empty and temperature is colder we append
            stk.append(index)
        return result

daily  = DailyTemperature()
print(daily.calculateWarmDays([73, 74, 75, 71, 69, 72, 76, 73]))
