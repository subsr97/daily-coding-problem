"""
#29
Amazon

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

"""

def encode(plaintext):
    encodedString = ""

    if not plaintext:
        return plaintext
    
    currentLetter = plaintext[0]
    repetitionCount = 1

    for letter in plaintext[1:]:
        if letter != currentLetter:
            encodedString += str(repetitionCount) + currentLetter
            currentLetter = letter
            repetitionCount = 1
        else:
            repetitionCount += 1
    
    encodedString += str(repetitionCount) + currentLetter

    return encodedString

# Parses string and returns the parsed number and remaining string
def parseNumber(string):
    numberString = ""
    stringList = list(string)

    while stringList:
        character = stringList.pop(0)
        if character.isnumeric():
            numberString += character
        else:
            stringList.insert(0, character)
            break

    return (int(numberString), "".join(stringList))

def decode(encodedString):
    decodedString = ""

    if not encodedString:
        return encodedString
    
    while encodedString:
        repetitionCount, encodedString = parseNumber(encodedString)
        letter = encodedString[0]
        encodedString = encodedString[1:]
        decodedString += (letter * repetitionCount)
    
    return decodedString


def main():
    plaintext = "AAAABBBCCDAA"
    print(plaintext)
    print(encode(plaintext))
    print(decode(encode(plaintext)))

if __name__ == "__main__":
    main()