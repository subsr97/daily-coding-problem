"""
#11
Twitter

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""
suggestions = []

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def add(self, remaining, word):
        exists = False
        
        for child in self.children:
            if remaining[0] == child.val:
                exists = True
                if len(remaining) > 1:
                    child.add(remaining[1:], word)
                else:
                    child.children.append(Node(word))
        
        if not exists:
            newNode = Node(remaining[0])
            self.children.append(newNode)
            if len(remaining) > 1:
                newNode.add(remaining[1:], word)
            else:
                newNode.children.append(Node(word))

    def findSuggestions(self):
        if self.children == []:
            suggestions.append(self.val)
        else:
            for child in self.children:
                child.findSuggestions()

    def find(self, query):
        if query == "":
            self.findSuggestions()
            return

        for child in self.children:
            if query[0] == child.val:
                return child.find(query[1:])
        
        return None


if __name__ == "__main__":
    root = Node("root")

    queryStrings = ["dog", "deer", "deal"]

    for query in queryStrings:
        root.add(query.lower(), query.lower())

    query = "de"

    root.find(query)

    print(suggestions)