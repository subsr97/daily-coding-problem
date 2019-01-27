"""
#166
Uber

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

"""

class TwoDIterator:
    def __init__(self, array):
        self.array = array
    
    def next(self):
        while True:
            try:
                element = self.array[0][0]

                if len(self.array[0]) == 1:
                    self.array = self.array[1:]
                else:
                    self.array[0] = self.array[0][1:]

                return element
            except Exception as e:
                if len(self.array) > 1:
                    self.array = self.array[1:]
                else:
                    raise e
    
    def has_next(self):
        while True:
            try:
                self.array[0][0]
                return True
            except:
                if len(self.array) > 1:
                    self.array = self.array[1:]
                else:
                    return False


def main():
    twoDIterator = TwoDIterator([[1, 2], [3], [], [4, 5, 6]])

    while twoDIterator.has_next():
        print(twoDIterator.next(), end=" ")
    
    # 1 2 3 4 5 6

    print()


    twoDIterator = TwoDIterator([[1, 2], [3], [], [4, 5, 6]])

    while True:
        try:
            print(twoDIterator.next(), end=" ")
        except Exception as e:
            print(e)
            break
    
    # 1 2 3 4 5 6 list index out of range
    

if __name__ == "__main__":
    main()
