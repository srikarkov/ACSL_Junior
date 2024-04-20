def acslTiles(rowNum, numString):
    rowNumArr = [rowNumIter for rowNumIter in str(rowNum)]
    numArr = numString.split()
    discardNum = 0
    checkToContinue = 0
    for number in numArr:
        checkToContinue = 0
        for arrayPos in range(len(rowNumArr)):
            if checkToContinue == 0:
                if number[0] == rowNumArr[arrayPos]:
                    rowNumArr[arrayPos] = number[1]
                    checkToContinue = 1
                elif number[1] == rowNumArr[arrayPos]:
                    rowNumArr[arrayPos] = number[0]
                    checkToContinue = 1
        if checkToContinue == 0:
            discardNum += int(number[0]) + int(number[1])
            checkToContinue = 1
    return discardNum
#up until here is the code written in HackerRank
answer = acslTiles(int(input()), input())
print(answer)