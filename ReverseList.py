def ReverseList(inputList):
    print inputList
    if len(inputList) == 1:
        if type(inputList[0]) != list:
            return inputList
        elif type(inputList[0]) == list:
            return ReverseList(inputList[0])
    elif type(inputList[-1]) != list:
        return [inputList[-1]] + ReverseList(inputList[:-1])
    elif type(inputList[-1]) == list:
        return [ReverseList(inputList[-1])] + ReverseList(inputList[:-1])

L = [1, 2, [31, 32], 4, [51, [521, 522], 53], 6]

print ReverseList(L)