inpt = input()
# number 1
inptArr = list(inpt)
for a in range(len(inpt)):
    char = inpt[a]
    if char.isalpha() == False:
        inptArr.remove(char)
inptmod1 = ''
for b in inptArr:
    inptmod1 = inptmod1 + b
inptmod1 = inptmod1.lower()

#number 2
inptmod2 = inptmod1
inptArr2 = list(inptmod1)
inptArr3 = inptArr2
array = []
array2 = []
while len(inptArr2) > 0:
    for c in inptmod2:
        if array.count(c) == 0:
            array.append(c)
            inptArr2.remove(c)
        array.sort()
    for d in array:
        array2.append(d)
    array = []
finalans = ''
for e in array2:
    finalans = finalans + e
print(len(finalans))