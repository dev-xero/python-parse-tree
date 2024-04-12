class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def setRootKey(self, key):
        self.key = key
    
    def insertLeft(self, newNode):
        subTree = BinaryTree(newNode)      
        if self.leftChild == None:
            self.leftChild = subTree
        else:
            subTree = BinaryTree(newNode)
            subTree.leftChild = self.leftChild
            self.leftChild = subTree
    
    def insertRight(self, newNode):
        subTree = BinaryTree(newNode)
        if self.rightChild == None:
            self.rightChild = subTree
        else:
            subTree.rightChild = self.rightChild
            self.rightChild = subTree

    def printNodes(self, node):
        root = node
        if root == None:
            return
        print(root.key, end=" ")
        if root.leftChild != None:
            self.printNodes(root.leftChild)
        if root.rightChild != None:
            self.printNodes(root.rightChild)
    
    def getRootKey(self):
        return self.key

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def modelTree(self, padding, pointer, node, treeBuilder=""):
        if node is None:
            return treeBuilder

        treeBuilder += padding + pointer + node.getRootKey() + '\n'
        nextPadding = "│  "
        rightPointer = "└──"
        leftPointer = "├──" if node.getRightChild() is not None else "└──"
        
        treeBuilder = self.modelTree(nextPadding, leftPointer, node.getLeftChild(), treeBuilder)
        treeBuilder = self.modelTree(nextPadding, rightPointer, node.getRightChild(), treeBuilder)
        
        return treeBuilder

def main():
    rootNode = BinaryTree("root")

    rootNode.insertLeft("node1")
    rootNode.insertRight("node2")

    rootNode.printNodes(rootNode)
    treeBuild = rootNode.modelTree("", "", rootNode)
    print(treeBuild)


if __name__ == "__main__":
    main()