"""
#157
Amazon

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.
"""

def isPermutationPalindrome(word):
    oddCountSet = set()
    
    """
    For every letter in word,
        -> If it's in oddCountSet, remove it.
        -> If it's not in oddCountSet, add it to the set.
    """
    for letter in word:
        if letter in oddCountSet:
            oddCountSet.remove(letter)
        else:
            oddCountSet.add(letter)
    
    # For palindromes, the number of odd count letters should be 0 or 1.
    return len(oddCountSet) == 0 or len(oddCountSet) == 1


def main():
    words = ["carrace", "daily"]

    for word in words:
        print(word, "-", isPermutationPalindrome(word))

if __name__ == "__main__":
    main()