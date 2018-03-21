
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            print("Value already exist.")

        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                print("Value added successfully!")
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                print("Value added successfully!")

    def find(self, data):
        if self.value == data:
            print("Found!")
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                print("Not Found!")
        else:
            if self.right:
                return self.right.find(data)
            else:
                print("Found!")

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            print("Root inserted!")

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            print("Tree is empty!")

    def preorder(self):
        if self.root is not None:
            print("PreOrder")
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            print("PostOrder")
            self.root.postorder()


bst = Tree()
bst.insert(30)
bst.insert(17)
bst.insert(7)
bst.insert(27)
bst.insert(11)
bst.preorder()
bst.inorder()
bst.postorder()
bst.find(17)
