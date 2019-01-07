"""
#121
Google

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""

def palindromable(word, k):
    start = 0
    end = len(word) - 1

    return palindromableHelper(word, k, start, end)

def palindromableHelper(word, k, x, y):
    if k < 0 :
        return False

    while x < y:
        if word[x] != word[y]:
            return palindromableHelper(word, k-1, x+1, y) or palindromableHelper(word, k-1, x, y-1)
        x += 1
        y -= 1

    return True

def main():
    print(palindromable("waterrfetawx", 2))
    print(palindromable("abcdefg", 1))
    print(palindromable("madam",0))

if __name__ == "__main__":
    main()
