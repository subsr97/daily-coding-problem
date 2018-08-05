"""
#22
Microsoft

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""
validSentences = []

def parseSentenceString(dictionary, sentenceString, currWords):
    currWord = ""

    if sentenceString == []:
        validSentences.append(currWords)
    
    for i in range(len(sentenceString)):
        letter = sentenceString[i]
        currWord += letter
        if currWord in dictionary:
            parseSentenceString(dictionary, sentenceString[i+1:], currWords+[currWord])
        
        

def findValidSentences(dictionary, sentenceString):
    global validSentences
    validSentences = []
    sentenceString = list(sentenceString)

    parseSentenceString(dictionary, sentenceString, [])

    if validSentences:
        return validSentences
    return None

if __name__ == "__main__":
    dictionary = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentenceString = "bedbathandbeyond"

    print(findValidSentences(dictionary, sentenceString))