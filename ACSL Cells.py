def program():
    inpt = input('give the input')
    inpt = inpt.split(', ')
    operation = inpt[0]
    string = inpt[1]
    if operation[0] == 'D' or operation[0] == 'd':
        cell1 = string[0] + string[1] + string[2] + string[3]
        cell2 = string[4] + string[5] + string[6] + string[7]
        cell1 = cell1 + cell1
        cell2 = cell2 + cell2
        printed = cell1 + ' and ' + cell2
    elif operation[0] == 'A' or operation[0] == 'a':
        n = int(operation[3])
        replicate = string[:n]
        printed = replicate + string
        printed = printed[:-3]
    elif operation[0] == 'S' or operation[0] == 's':
        n = int(operation[8])
        replicate = string[-n:]
        printed = string+replicate
        printed = printed[n:]
    print(printed)
for x in range(0,5):
    program()