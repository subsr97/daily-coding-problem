"""
#188
Google

This problem was asked by Google.

What will this code print out?

    def make_functions():
        flist = []

        for i in [1, 2, 3]:
            def print_i():
                print(i)
            flist.append(print_i)

        return flist

    functions = make_functions()
    for f in functions:
        f()

How can we make it print out what we apparently want?
"""

def make_functions():
    flist = []

    for i in [1,2,3]:
        def print_i():
            print(i)
        flist.append(print_i)
    
    return flist

def make_functions_modified():
    flist = []

    for i in [1,2,3]:
        def print_i(i=i):
            print(i)
        flist.append(print_i)
    
    return flist

def make_lambdas():
    llist = []

    for i in [1,2,3]:
        llist.append(lambda i=i: print(i))
    
    return llist

def main():
    functions = make_functions()
    for f in functions:
        f()
    """
    Output:
    3
    3
    3

    Explanation:
    The variable i in line 31 refers to the variable i in the outer scope (i.e) line 29.
    """
    print()

    functions = make_functions_modified()
    for f in functions:
        f()
    """
    Output:
    1
    2
    3

    Explanation:
    Pass i as an argument to the print_i() function so that the i in line 31 will refer to that parameter rather than the outer i.
    """
    print()

    lambdas = make_lambdas()
    for l in lambdas:
        l()
    """
    Output:
    1
    2
    3

    Explanation:
    Use lambdas to achieve the same functionality using anonymous functions.
    """
    

if __name__ == "__main__":
    main()