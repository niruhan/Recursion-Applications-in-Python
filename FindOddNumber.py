def FindOddNumber(NumberList):
    global answerList
    length = len(NumberList)
    if length == 0:
        return
    if length == 1:
        answerList.append(NumberList[0])
        return
    else:
        mid = length/2
        if NumberList[mid] == NumberList[mid-1]:
            FindOddNumber(NumberList[:mid - 1])
            FindOddNumber(NumberList[mid + 1:])
            return
        elif length == 2:
            answerList = answerList + NumberList
        elif NumberList[mid] == NumberList[mid+1]:
            FindOddNumber(NumberList[:mid])
            FindOddNumber(NumberList[mid + 2:])
            return
        else:
            answerList.append(NumberList[mid])
            return

a = [ 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6]

answerList = []

FindOddNumber(a)

a = answerList
answerList =[]
FindOddNumber(a)

print answerList