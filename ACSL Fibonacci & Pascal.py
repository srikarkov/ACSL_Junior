fibNumber = input()
if fibNumber == 1:
    answer = '1'
else:
    fibArr = [0, 1]
    diagNum = -1
    numbersike = -1
    while numbersike != fibNumber:
        numbersike = fibArr[-2] + fibArr[-1]
        fibArr.append(numbersike)
        diagNum = diagNum + 1
    diagArr = []
    for a in range(1,diagNum+1):
        diagArr.append(a)
    numCountmod = diagNum % 2
    if numCountmod == 1:
        numCount = int((diagNum+3)/2)
    else:
        numCount = int((diagNum+2)/2)

    array = diagArr[1:]
    newArr = []
    number = diagNum - 2
    ansArr = [1, diagNum]
    for b in range(numCount-2):
        newArr = [1]
        for c in range(number-1):
            appendto = newArr[-1] + array[c]
            newArr.append(appendto)
        ansArr.append(newArr[-1])
        array = newArr[1:]
        number = number - 2
    answer = ''
    for d in ansArr:
        answer = answer + ' ' + str(d)
    answer = answer.strip()
