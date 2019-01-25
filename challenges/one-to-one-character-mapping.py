"""
#176
Bloomberg

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""

def formCharCountMap(s):
    charCountMap = dict()
    
    for letter in s:
        if letter in charCountMap.keys():
            charCountMap[letter] += 1
        else:
            charCountMap[letter] = 1
    
    return charCountMap
    
def formInvertedCountMap(charCountMap):
    invertedCountMap = dict()

    for letter in charCountMap:
        count = charCountMap[letter]
        if count in invertedCountMap:
            invertedCountMap[count] += 1
        else:
            invertedCountMap[count] = 0
    
    return invertedCountMap

def oneToOneCharacterMapping(s1, s2):
    s1CharCountMap = formCharCountMap(s1)
    s2CharCountMap = formCharCountMap(s2)

    s1InvertedCountMap = formInvertedCountMap(s1CharCountMap)
    s2InvertedCountMap = formInvertedCountMap(s2CharCountMap)

    return s1InvertedCountMap == s2InvertedCountMap

def main():
    s1 = "abc"
    s2 = "bcd"
    print(oneToOneCharacterMapping(s1, s2))

    s1 = "foo"
    s2 = "bar"
    print(oneToOneCharacterMapping(s1, s2))

if __name__ == "__main__":
    main()
