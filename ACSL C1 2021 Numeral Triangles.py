val1 = int(input('give the first value'))# s starting number
val2 = int(input('give the second value'))# d increased by
val3 = int(input('give the third value'))# r number of rows

def sumOfLastRow(s, d, r):
    addVal = 0
    for x in range(r, 0, -1):
        addVal = addVal + x

    allValArr = []
    value = s
    while len(str(value)) > 1:
        value2 = value
        value = 0
        for a in str(value2):
            value = value + int(a)
    for y in range(0, addVal):
        if y == 0:
            allValArr.append(value)
        else:
            value = value + d
            while len(str(value)) > 1:
                value3 = value
                value = 0
                for a in str(value3):
                    value = value + int(a)
            allValArr.append(value)
    sumArr = allValArr[-r:]
    sum1 = sum(sumArr)
    print(allValArr)
    print(sumArr)
    print(sum1)
        
sumOfLastRow(val1, val2, val3)