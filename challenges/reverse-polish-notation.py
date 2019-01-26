"""
#163
Jane Street

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

class Stack:
    def __init__(self):
        self.array = []
    
    def push(self, val):
        self.array.append(val)
    
    def pop(self):
        if len(self.array):
            return self.array.pop()
        else:
            return None

def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate(exprList):
    operators = ['+', '-', '*', '/']

    evalStack = Stack()

    for token in exprList:
        if token in operators:
            operand2 = evalStack.pop()
            operand1 = evalStack.pop()
            evalStack.push(calculate(operand1, operand2, token))
        else:
            evalStack.push(token)
    
    return evalStack.pop()

def main():
    expressionList = [5, 3, '+']
    print(evaluate(expressionList))

    expressionList = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
    print(evaluate(expressionList))

if __name__ == "__main__":
    main()
