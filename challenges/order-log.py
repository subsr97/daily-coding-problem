"""
#16
Twitter

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    -> record(order_id): adds the order_id to the log  
    -> get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

"""

orderLog = []
N = 5

def record(orderID):
    if len(orderLog) == N:
        orderLog.pop(0)
    orderLog.append(orderID)

def get_last(position):
    if position <= N and position <= len(orderLog) :
        return orderLog[position*-1]
    else:
        return None

def showLog():
    print(*orderLog)

if __name__ == "__main__":

    choice = -1

    print("1. Record\n2. Get Last\n3. Show log\n4. Exit")

    while True:
        
        choice = int(input("\nEnter your choice:").strip())
        
        if choice == 1:
            orderID = int(input("Enter the order ID:").strip())
            record(orderID)

        elif choice == 2:
            position = int(input("Enter the position").strip())
            print(get_last(position))

        elif choice == 3:
            showLog()

        elif choice == 4:
            exit(0)

        else:
            print("Invalid choice.")
