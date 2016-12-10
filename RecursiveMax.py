def RecursiveMax(inputList):
    # print inputList[0]
    if len(inputList) == 1:
        if type(inputList[0]) == int:
            return inputList[0]
        elif type(inputList[0]) == list:
            return RecursiveMax(inputList[0])
    elif type(inputList[0]) == int:
        return max(inputList[0], RecursiveMax(inputList[1:]))
    elif type(inputList[0]) == list:
        return max(RecursiveMax(inputList[0]), RecursiveMax(inputList[1:]))
    elif type(inputList[0]) == str:
        return RecursiveMax(inputList[1:])


t1 = [2, 4, 6, 8, [[11, "tu"], 10, [9, 7]], 5, 3, "ccc", 1]

mx = RecursiveMax(t1)

print mx
