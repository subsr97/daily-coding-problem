"""
#7
Facebook

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

allMessages = []

def decode(parsed, remaining):
    if remaining == "":
        if parsed not in allMessages:
            allMessages.append(parsed)
        else:
            print(parsed)
        return

    singleDigit = int(remaining[0])
    if singleDigit in range(1,27):
        decode(parsed+[singleDigit], remaining[1:])

    if len(remaining)>1:
        twoDigits = int(remaining[0:2])
        if twoDigits in range(1,27):
            decode(parsed+[twoDigits], remaining[2:])

if __name__ == "__main__":
    message = input().strip()
    decode([], message)
    print(len(allMessages))
