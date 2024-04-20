def program():
    inpt = input('give the input ')
    inptArr = inpt.split(' ')
    poslet = int(inptArr[0])

    string = ''
    for z in range(1,len(inptArr)):
        string = string + inptArr[z].lower()
    stringer2 = ''
    for y in string:
        if y.isalpha():
            stringer2 = stringer2 + y
    string = stringer2

    answerArr = []
    stringArr = list(string)
    charArr = []
    for x in range(poslet):
        char = stringArr[0]
        charArr.append(char)
        charArr = sorted(charArr)
        stringArr.remove(char)
        if x == poslet - 1:
            answerArr.append(charArr[poslet-1])

    for w in range(len(stringArr)):
        character = stringArr[w]
        charArr.append(character)
        charArr = sorted(charArr)
        answer = charArr[poslet-1]
        answerArr.append(answer)

    countArr = []
    for v in answerArr:
        countof = countArr.count(v)
        if countof == 0:
            countArr.append(v)
    theFinalAnswer = len(countArr)
    print(theFinalAnswer)

for programdone in range(5):
    program()