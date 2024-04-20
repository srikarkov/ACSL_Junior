def program():
    inpt = input('give the input')
    parloc1 = inpt.find('(')#finds position of parentheses
    parloc2 = inpt.find(')')#finds position of parentheses
    if parloc1 != -1:
        restofstr = inpt[:parloc1]
        parwthout = inpt[(parloc1+1):]# gives number without parentheses
        #parrev = parwthout[::-1]#reverses string
        parArr = []#makes the string an Array
        for y in parwthout:
            parArr.append(y)
        parArr = parArr[1:]#makes the last element/character go away
        for x in range(0, len(parArr)):
            xofArr = parArr[x]
            if xofArr.isnumeric():
                if parArr[x-1] == '+' or parArr[x-1] == '-' or parArr[x-1] == '*' or parArr[x-1] == '/' or parArr[x-1] == '–':
                    almostAns = len(restofstr) + x
                    print(almostAns+4)#adding one because finding is one less. adding one to account for parentheses. adding one to account for the first number. adding one because we replace it with the one after.

    elif parloc2 != -1:
        parwthout = inpt[:parloc2]# gives number without parentheses
        #parrev = parwthout[::-1]#reverses string
        parArr = []#makes the string an Array
        for y in parwthout:
            parArr.append(y)
        parArr = parArr[:-1]#makes the last element/character go away
        for x in range(0, len(parArr)):
            xofArr = parArr[x]
            if xofArr.isnumeric():
                if parArr[x+1] == '+' or parArr[x+1] == '-' or parArr[x+1] == '*' or parArr[x+1] == '/' or parArr[x+1] == '–':
                    print(x+1)


for letsgo in range(0,5):
    program()