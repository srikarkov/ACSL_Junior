#get the input from the user, and split the SWC list into individual groups
textInput = input()
swcStr = input()
swcList = swcStr.split()

#making a sentence list
text2DList = []
sentenceList = textInput.split(".  ")

#making a 2D array with words in a sentence array, and sentences in the whole array
for sentence in sentenceList:
    text2DList.append(sentence.split())
    
#removing the period from the last word in the last sentence
text2DList[-1][-1] = (text2DList[-1][-1])[:-1]

#making the function to retrieve the character from the paragraph
def getCharacter(sentenceWordChar):
    #seperate the sentence number, word number, and character number
    sentencePos, wordPos, charPos = sentenceWordChar.split(".")
    #making it an index by reducing by one so it will not go one over
    sentencePos, wordPos, charPos = int(sentencePos)-1, int(wordPos)-1, int(charPos)-1
    #checking to see if the needed sentence/word/character is past the index of the array
    #If so, return a space.
    if sentencePos >= len(text2DList):
        return " "
    elif wordPos >= len(text2DList[sentencePos]):
        return " "
    elif charPos >= len(text2DList[sentencePos][wordPos]):
        return " "
    #If not, return the needed character using indexing
    else:
        return text2DList[sentencePos][wordPos][charPos]
#making an answer variable
answer = ""
#adding each character from the getCharacter function into the answer string
for swc in swcList:
    answer += getCharacter(swc)
#printing the answer
print(answer)