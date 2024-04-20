def acslAgram(inpt):
    #splitting the input into different letters and numbers
    inptLetArr = inpt.split(', ')
    #print(inptLetArr)
    #organizing the characters into cards and variables
    LeadCrd = inptLetArr[0] + inptLetArr[1]
    LdCrdNum = LeadCrd[0]
    LdCrdSt = LeadCrd[1]
    card1 = inptLetArr[2] + inptLetArr[3]
    card2 = inptLetArr[4] + inptLetArr[5]
    card3 = inptLetArr[6] + inptLetArr[7]
    card4 = inptLetArr[8] + inptLetArr[9]
    card5 = inptLetArr[10] + inptLetArr[11]
    #making an array with all the possible cards
    inptArr = [card1, card2, card3, card4, card5]
    #defining arrays used later like cards with suit, cards bigger, and cards smaller
    suitArr = []
    bigCrdArr = []
    smllCrdArr = []
    answer = ""
    #seeing if any cards match suit with lead card and append to list
    for card in inptArr:
        if LdCrdSt == card[1]:
            suitArr.append(card)
    #if there are any cards that match suit, go ahead with the code
    if len(suitArr) > 0:
        #if only one card in suit, print it because it is lowest
        if len(suitArr) == 1:
            answer = suitArr[0]
        #if there is more than 1 card in the suit, go ahead with code
        elif len(suitArr) > 1:
            #sorting through all the suitCards and putting them in lists based on num value
            for suitCard in suitArr:
                if int(suitCard[0]) > int(LdCrdNum):
                    bigCrdArr.append(suitCard)
                elif int(suitCard[0]) <= int(LdCrdNum):
                    smllCrdArr.append(suitCard)
            #if there are no cards with a number bigger, then find the smallest
            if len(bigCrdArr) == 0:
                #defining minimum as the first card (have to start somewhere right?)
                minimum = int((smllCrdArr[0])[0])
                for card in smllCrdArr:
                    #if the card num is same or smaller, then that will be the new winCard
                    if int(card[0]) <= minimum:
                        minimum = int(card[0])
                        winCard = card
                    #if smllCrdArr.index(card) == len(smllCrdArr)-1:
                answer = winCard
            
            elif len(bigCrdArr) > 0:
                minimum = int((bigCrdArr[0])[0])
                for card in bigCrdArr:
                    number = int(card[0])
                    if number <= minimum:
                        minimum = int(card[0])
                        winCard = card
                    if bigCrdArr.index(card) == len(bigCrdArr)-1:
                        answer = winCard
    #if there are no cards that match suit, print "NONE"
    else:
        answer = ("NONE")
    #if the length of the answer is 2 (if the answer is a card), then add a comma in between
    if len(answer) == 2:
        answer = answer[0] + ", " + answer[1]
    return answer
    
def runProg():
    outputArr = []
    for iterate in range(5):
        outputArr.append(acslAgram(input("Provide the input: ")))
    for resultPos in range(5):
        print(outputArr[resultPos])

runProg()
