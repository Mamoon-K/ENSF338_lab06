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
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


def tokenize(expression):
    tokens = expression.split()
    return tokens

# extract_subexpression function suggested by ChatGPT after giving it my attempt at counting the 
# parentheses
def extract_subexpression(tokens, start_index):
    """Extracts a subexpression enclosed in parentheses."""
    open_parens = 0
    for i in range(start_index, len(tokens)):
        if tokens[i] == "(":
            open_parens += 1
        elif tokens[i] == ")":
            open_parens -= 1
            if open_parens == 0:
                return tokens[start_index+1:i], i
    return [], start_index  # If unmatched parentheses exist

def parseTokensToTree(tokens):
    if len(tokens) == 1 and tokens[0].isdigit():
        return Tree(Node(tokens[0]))

    index = 0
    leftTree = None  # Start with no tree

    while index < len(tokens):
        token = tokens[index]
        if token in "+-*/":
            tree = Tree(Node(token))

            # We handle the left operand
            if index > 0: 
                if tokens[index - 1].isdigit():
                    tree.root.setLeft(Node(tokens[index - 1]))
                elif tokens[index - 1] == ")" and leftTree:
                    # Set the left side of our new tree to the tree we have been building up
                    tree.root.setLeft(leftTree.root)

            # We handle the right operand
            if index + 1 < len(tokens):
                if tokens[index + 1].isdigit():
                    tree.root.setRight(Node(tokens[index + 1]))
                elif tokens[index + 1] == "(":
                    subexpr, new_index = extract_subexpression(tokens, index + 1)
                    tree.root.setRight(parseTokensToTree(subexpr).root)
                    index = new_index 

            leftTree = tree  # Update leftTree for the next operator we find
        index += 1

    return leftTree if leftTree else Tree(Node(tokens[0]))

def evaluateTree(root):
    if root:
        evaluateTree(root.left)
        evaluateTree(root.right)
        if root.left != None and root.right != None:
            if root.data == "+":
                root.data = float(root.left.data) + float(root.right.data)
            if root.data == "-":
                root.data = float(root.left.data) - float(root.right.data)
            if root.data == "*":
                root.data = float(root.left.data) * float(root.right.data)
            if root.data == "/":
                root.data = float(root.left.data) / float(root.right.data)
        
        if root.parent == None:
            if root.data == 0:
                return 0
            if type(root.data) == float:
                if root.data.is_integer():
                    return int(root.data)
            return root.data

argsInRaw = " ".join(sys.argv[1:])
tokens = tokenize(argsInRaw)
outputTree = parseTokensToTree(tokens)
print(evaluateTree(outputTree.root))