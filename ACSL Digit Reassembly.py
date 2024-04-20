inpt1 = input()
inpt2 = input()
inpt3 = input()
inpt4 = input()
inpt5 = input()

ans1 = len(inpt1)

ans2 = 0
for dig in inpt2:
    ans2 = ans2 + int(dig)

ans3 = 0
for dig2 in range(0,len(inpt3),2):
    ans3 = ans3 + int(inpt3[dig2])

ans4 = inpt4.count("4")

if len(inpt5)/2 == int(len(inpt5)/2):
    mid = int(len(inpt5)/2) - 1
else:
    mid = int(len(inpt5)/2)
ans5 = inpt5[mid]


print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
