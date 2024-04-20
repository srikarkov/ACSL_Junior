strtstr = input('give the string')
def program(strtstr):
    inpt = input('give the input')
    findcom = inpt.find(', ')
    if findcom != -1:
        inptArr = inpt.split(', ')
    else:
        inptArr = inpt.split(',')
    start = int(inptArr[0])
    length = int(inptArr[1])
    string = strtstr[start:]
    if length > 0:
        string = string[:length]
    elif length < 0:
        string = string[:length]
    elif length == 0:
        string = string
    print(string)
for x in range(0,8):
    program(strtstr)