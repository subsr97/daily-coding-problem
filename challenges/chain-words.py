"""
#246
Dropbox

Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic'] can form the following circle:
chair --> racket --> touch --> height --> tunic --> chair.

"""

def checkForCycleHelper(usedWords, remainingWords):
    if len(remainingWords) == 0:
        # print(usedWords, end=" ")     # Uncomment to see the chain
        return True
    
    lastLetter = usedWords[-1][-1]
    for i in range(len(remainingWords)):
        nextWord = remainingWords[i]
        if nextWord.startswith(lastLetter) and checkForCycleHelper(usedWords+[nextWord], remainingWords[:i]+remainingWords[i+1:]):
            return True
    
    return False


def checkForCycle(words):
    return checkForCycleHelper([words[0]], words[1:])

def main():
    print(checkForCycle(["geek", "king"]))                      # True ['geek', 'king']
    print(checkForCycle(["for", "geek", "rig", "kaf"]))         # True ['for', 'rig', 'geek', 'kaf']
    print(checkForCycle(["aab", "bac", "aaa", "cda"]))          # True ['aab', 'bac', 'cda', 'aaa']
    print(checkForCycle(["aaa", "bbb", "baa", "aab"]))          # True ['aaa', 'aab', 'bbb', 'baa']
    print(checkForCycle(["aaa"]))                               # True ['aaa']
    print(checkForCycle(["aaa", "bbb"]))                        # False
    print(checkForCycle(["abc", "efg", "cde", "ghi", "ija"]))   # True ['abc', 'cde', 'efg', 'ghi', 'ija']
    print(checkForCycle(["ijk", "kji", "abc", "cba"]))          # False


if __name__ == "__main__":
    main()