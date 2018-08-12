"""
#28
Palantir

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:
    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly

"""

# Using "-" instead of " " for clarity in output
def justify(wordList, k):
    print(wordList)
    justifiedLineList = []

    currentWordList = []
    currentLength = 0

    while True:
        newWordFlag = False

        if wordList:
            newWordFlag = True
            currentWord = wordList.pop(0)
        
        if currentLength + len(currentWord) + 1 <= k+1 and newWordFlag:
            currentWordList.append(currentWord)
            currentLength += len(currentWord) + 1
        else:
            unusedSpace = k-(currentLength-1)

            try:
                extraEvenSpaces = unusedSpace // (len(currentWordList)-1)
            except:
                break

            currentSpaceList = ["-"]*(len(currentWordList)-1)

            for i in range(len(currentSpaceList)):
                currentSpaceList[i] += "-"*extraEvenSpaces

            extraUnevenSpaces = unusedSpace%len(currentSpaceList)

            for i in range(extraUnevenSpaces):
                currentSpaceList[i] += "-"

            currentLine = ""

            while currentSpaceList:
                currentLine += currentWordList.pop(0) + currentSpaceList.pop(0)
            currentLine += currentWordList.pop(0)
            
            justifiedLineList.append(currentLine)

            if newWordFlag:
                currentWordList = [currentWord]
                currentLength = len(currentWord) + 1
            
            if not wordList:
                break
    
    if currentWordList:
        lastLine = currentWordList[0] + "-"*(k-len(currentWordList[0]))
        justifiedLineList.append(lastLine)

    return justifiedLineList

def printJustifiedText(justifiedLineList):
    for line in justifiedLineList:
        print(line)
    print()

def main():
    wordList = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16

    while wordList:
        tempWordList = wordList[:]
        printJustifiedText(justify(tempWordList, k))
        wordList.pop()

if __name__ == "__main__":
    main()