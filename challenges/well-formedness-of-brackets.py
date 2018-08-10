"""
#27
Facebook

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

"""
def checkWellFormedness(bracketString):
    bracketStack = []
    openingBrackets = {"(", "{", "["}

    matchingBracketsDict = {")":"(", "]":"[", "}":"{"}

    for bracket in bracketString:
        if bracket in openingBrackets:
            bracketStack.append(bracket)
        else:
            if bracketStack and bracketStack[-1] == matchingBracketsDict[bracket]:
                bracketStack.pop()
            else:
                return False
    
    return not bracketStack

def main():
    print(checkWellFormedness("([])[]({})"))
    print(checkWellFormedness("([)]"))
    print(checkWellFormedness("((()"))

if __name__ == "__main__":
    main()