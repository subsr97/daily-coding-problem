"""
#3
Google

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
import json

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.serializedTree = dict()

    def __str__(self):
        return "< " + str(self.val) + ", " + str(self.left) + ", " + str(self.right) + " >"


def serializeNode(node):
    node.serializedTree["val"] = node.val

    if node.left != None:
        node.serializedTree["left"] = serializeNode(node.left)
    else:
        node.serializedTree["left"] = None

    if node.right != None:
        node.serializedTree["right"] = serializeNode(node.right)
    else:
        node.serializedTree["right"] = None

    return node.serializedTree

def serialize(node):
    return json.dumps(serializeNode(node))

def deserialize(s):
    nodeJson = json.loads(s)
    if nodeJson["left"] != None and nodeJson["right"] != None:
        return Node(nodeJson["val"], deserialize(json.dumps(nodeJson["left"])), deserialize(json.dumps(nodeJson["right"])))
    elif nodeJson["left"] != None:
        return Node(nodeJson["val"], deserialize(json.dumps(nodeJson["left"])))
    elif nodeJson["right"] != None:
        return Node(nodeJson["val"], None, deserialize(json.dumps(nodeJson["right"])))
    else:
        return Node(nodeJson["val"])

if __name__ == "__main__":
    n = Node('root', Node('left', Node('left.left')), Node('right'))
    print(deserialize(serialize(n)).left.left.val == "left.left")
