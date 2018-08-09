"""
#25
Facebook

Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not
the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true.
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.

"""

matched = False

def match(regex, string):
    
    global matched

    if regex == "" and string == "":
        matched = True
        return
    elif regex == "" or string == "":
        matched = False
        return
    
    if len(regex) >= 2 and regex[1] == "*":
        front = 0
        try:
            while string[front] == regex[0] or regex[0] == ".": 
                match(regex[2:], string[front:])
                front += 1
            match(regex[2:], string[front:])
        except:
            pass
    else:
        if regex[0] == ".":
            match(regex[1:], string[1:])
        else:
            if regex[0] == string[0]:
                match(regex[1:], string[1:])
            else:
                return

def matchRegex(regex, string):
    global matched
    matched = False
    match(regex,string)
    return matched

def main():
    print(matchRegex("ra.", "ray"))         # True
    print(matchRegex("ra.", "raymond"))     # False
    print(matchRegex(".*at", "chat"))       # True
    print(matchRegex(".*at", "chats"))      # False

if __name__ == "__main__":
    main()