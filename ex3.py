import sys

class Node:
    def __init__ (self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def setData(self, data):
        self.data = data

    def setParent(self, parent):
        self.parent = parent

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class Tree:
    def __init__ (self, root=None):
        self.root = root

    def setRoot(self, root):
        self.root = root

    def isEmpty (self):
        return self.root == None
    
    def postorder (self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

def tokenize(expression):
    tokens = argsInRaw.split()
    return tokens

def parseTokensToTree(tokens):
    if (len(tokens) == 1):
        if (tokens[0].isdigit()):
            # If the only token is a digit, return a tree with the topmost node being that number
            return Tree(Node(tokens[0]))
    
    index = 0
    outputTree = None
    leftTree = Tree()
    rightTree = Tree()
    for token in tokens:
        if token in "+-*/":
            tree = Tree(Node(token))
            if tokens[index - 1].isdigit():
                tree.root.setLeft(Node(tokens[index - 1]))
            elif tokens[index - 1] == ")":
                tree.root.setLeft(Node(leftTree.root))
            
            if tokens[index + 1].isdigit():
                tree.root.setRight(Node(tokens[index + 1]))
            """
            IMPLEMENT THIS FOR WHEN THERE ARE EXPRESSIONS TO THE RIGHT OF AN OPERATOR
            elif tokens[index + 1] == "(":
                # This returns a tree
                parseTokensToTree(tokens[index:])
            """

            leftTree = tree
        index += 1
        
    outputTree = leftTree
    return outputTree

    

argsInRaw = " ".join(sys.argv[1:])
tokens = tokenize(argsInRaw)
outputTree = parseTokensToTree(tokens)
print(outputTree.postorder(outputTree.root))