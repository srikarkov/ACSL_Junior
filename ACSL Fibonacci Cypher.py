key = input()
msg = input()
length = len(msg)
orgfib = [1,2]
for a in range(length-2):
    orgfibn1 = orgfib[-2]
    orgfibn2 = orgfib[-1]
    fibnext = orgfibn1 + orgfibn2
    orgfib.append(fibnext)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaArr = list(alphabet)
keypos = alphaArr.index(key)
fiboffset = []
for b in orgfib:
    plus = keypos + b
    if plus > 25:
        while plus > 25:
            adjusted = plus - 26
            plus = plus - 26
    else:
        adjusted = plus
    fibofflet = alphaArr[adjusted]
    fiboffset.append(fibofflet)
offasciiArr = []
for c in fiboffset:
    offascii = ord(c)
    offasciiArr.append(offascii)
strasciiArr = []
for d in msg:
    strascii = ord(d)
    strasciiArr.append(strascii)
calcArr = []
for e in range(length):
    offval = offasciiArr[e]
    strval = strasciiArr[e]
    calc = str(int(offval) + int(strval))
    calcArr.append(calc)
finalans = calcArr[0]
for f in range(1,len(calcArr)):
    finalans = finalans + " " + calcArr[f]
print(finalans)
#decoding the encoded message - not required but I feel like doing it.
'''
key = input()
msg = input()
length = len(msg)
orgfib = [1,2]
for a in range(length-2):
    orgfibn1 = orgfib[-2]
    orgfibn2 = orgfib[-1]
    fibnext = orgfibn1 + orgfibn2
    orgfib.append(fibnext)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaArr = list(alphabet)
keypos = alphaArr.index(key)
fiboffset = []
for b in orgfib:
    plus = keypos + b
    if plus > 25:
        while plus > 25:
            adjusted = plus - 26
            plus = plus - 26
    else:
        adjusted = plus
    fibofflet = alphaArr[adjusted]
    fiboffset.append(fibofflet)
'''