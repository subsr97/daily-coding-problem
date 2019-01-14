"""
# 182
Facebook

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected.
For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""

def hasCycleHelper(adjacencyMatrix, visitedNodes):
    # print(visitedNodes)
    for nodeIndex in range(len(adjacencyMatrix)):
        if adjacencyMatrix[visitedNodes[-1]][nodeIndex] == 1:
            if nodeIndex in visitedNodes[:-2]:
                # print(visitedNodes, nodeIndex)
                return True
            if len(visitedNodes) > 1 and nodeIndex == visitedNodes[-2]:
                continue
            if hasCycleHelper(adjacencyMatrix, visitedNodes+[nodeIndex]):
                # print(visitedNodes, nodeIndex)
                return True
    return False
            

def hasCycle(adjacencyMatrix):
    return hasCycleHelper(adjacencyMatrix, [0])


def isMinimallyConnected(adjacencyMatrix):
    """
        Checking for isolated vertices, parallel edges and self loops
        Max(row) == 0           =>  Isolated Vertex
        Max(row) > 1            =>  Parallel Edge
        Max([row[i][i]]) != 0   =>  Self Loop 
    """
    if min([max(row) for row in adjacencyMatrix]) != 1 or max([max(row) for row in adjacencyMatrix]) != 1 or max([adjacencyMatrix[i][i] for i in range(len(adjacencyMatrix))]) != 0:
        return False

    # Checking for cycles
    return not hasCycle(adjacencyMatrix)


def main():
    """
    Minimally connected graph
            0
           / \
          /   \
         1     2
        / \
       /   \
      3     4
    """
    adjacencyMatrix = [
       # 0  1  2  3  4
        [0, 1, 1, 0, 0], #0
        [0, 0, 0, 1, 1], #1
        [1, 0, 0, 0, 0], #2
        [0, 1, 0, 0, 0], #3
        [0, 1, 0, 0, 0], #4
    ]
    print(isMinimallyConnected(adjacencyMatrix)) # True


    """
    Graph with cycle
            0
           / \
          /   \
         /     \
        1 — — — 2
    """
    adjacencyMatrix = [
       # 0  1  2
        [0, 1, 1], #0
        [1, 0, 1], #1
        [1, 1, 0], #2
    ]
    print(isMinimallyConnected(adjacencyMatrix)) # False

    """
    Graph with parallel edge
         — — 0
        |   / \
        |  /   \
        | /     \
        1        2
    """
    adjacencyMatrix = [
       # 0  1  2
        [0, 2, 1], #0
        [2, 0, 0], #1
        [1, 0, 0], #2
    ]
    print(isMinimallyConnected(adjacencyMatrix)) # False

    """
    Graph with self loop
            0
           / \
          /   \
         /     \
        1       2 — —
                |    |
                |    |
                 — — —                
    """
    adjacencyMatrix = [
       # 0  1  2
        [0, 1, 1], #0
        [1, 0, 0], #1
        [1, 0, 1], #2
    ]
    print(isMinimallyConnected(adjacencyMatrix)) # False

    """
    Graph with isolated vertex
            0
           /
          /
        1          3 
         \
          \
           2
    """
    adjacencyMatrix = [
       # 0  1  2  3
        [0, 1, 0, 0], #0
        [1, 0, 1, 0], #1
        [0, 1, 0, 0], #2
        [0, 0, 0, 0], #3
    ]
    print(isMinimallyConnected(adjacencyMatrix)) # False


if __name__ == "__main__":
    main()
