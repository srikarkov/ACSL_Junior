finalArr = []
for progLoop in range(5):
    lineinput = input("Please provide the input: ")
    npdarray = lineinput.split()
    number = npdarray[0]
    numlist = [int(dig) for dig in number]
    numpos = int(npdarray[1])
    arithNum = int(npdarray[2])
    posdig = numlist[-numpos]
    
    if (posdig>=0) and (posdig<=4):
        numlist[-numpos] = int(str(posdig + arithNum)[-1])

    else:
        numlist[-numpos] = int(str(abs(posdig-arithNum))[0])
    if numpos!=1:    
        numlist = numlist[:(-numpos+1)]
    for iternum in range(numpos-1):
        numlist.append(0)
    numlistStr = list(map(str,numlist))#[str(dig) for dig in numlist]
    result = "".join(numlistStr)
    finalArr.append(result)
for loopnum in range(5):
    print(finalArr[loopnum])



'''
def writeToFile():
    file = open("testdata.txt", "w")
    file.write("4318762 4 3\n")
    file.write("72431685 1 7\n")
    file.write("123456789 7 8\n")
    file.write("9876543210 10 25\n")
    file.write("314159265358 8 428\n")
    file.close()

def numberTransformation(lineinput):
    npdarray = lineinput.split()
    number = npdarray[0]
    numlist = [int(x) for x in number]
    numpos = int(npdarray[1])
    transint = int(npdarray[2])
    pthOfn = numlist[-p]
    
    if (pthOfn>=0) and (pthOfn<=4):
        numlist[-p] = int(str(pthOfn + d)[-1])

    else:
        numlist[-p] = int(str(abs(pthOfn-d))[0])
    if p!=1:    
        numlist = numlist[:(-p+1)]
    for iternum in range(p-1):
        numlist.append(0)
    numlistStr = list(map(str,numlist))#[str(x) for x in numlist]
    result = "".join(numlistStr)

def executeProg():
    with open("testdata.txt") as fileused:
        for line in fileused:
            answer = numberTransformation(line)
            print(answer)
writeToFile()
executeProg()
'''