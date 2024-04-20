realPartC = float(input())
imagPartC = float(input())
def addition(a,b,c,d):
    aplusc = (a + c)
    bplusd = (b + d)
    plusArr = [aplusc,bplusd]
    return plusArr
def squaring(a,b):
    squTerm1 = (a**2)-(b**2)
    squTerm2 = (a*b)+(b*a)
    squTermArr = [squTerm1,squTerm2]
    return squTermArr
def absoluteVal(a,b):
    import math
    original = (a**2)+(b**2)
    absval = math.sqrt(original)
    return absval
def fofz(a,b,c,d):
    squareres = squaring(a,b)
    a2 = squareres[0]
    b2 = squareres[1]
    addres = addition(a2,b2,c,d)
    next1 = addres[0]
    next2 = addres[1]
    absvalnext = absoluteVal(next1,next2)
    nextArr = [next1,next2,absvalnext]
    return nextArr
x = 0.0
y = 0.0
checking = 0
count = 0    
for g in range(1,6):
    array = fofz(x,y,realPartC, imagPartC)
    x = array[0]
    y = array[1]
    absforprog = array[2]
    if absforprog > 4.0:
        answer = "ESCAPES " + str(g)
        checking = 1
        break
if g == 5 and checking == 0:
    answer = (str(round(absforprog,3)))
print(answer)