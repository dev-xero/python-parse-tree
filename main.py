class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def setRootKey(self, key):
        self.key = key
    
    def insertLeft(self, subTree):
        # subTree = BinaryTree(newNode)      
        if self.leftChild == None:
            self.leftChild = subTree
        else:
            subTree = BinaryTree(newNode)
            subTree.leftChild = self.leftChild
            self.leftChild = subTree
        return subTree
    
    def insertRight(self, subTree):
        # subTree = BinaryTree(newNode)
        if self.rightChild == None:
            self.rightChild = subTree
        else:
            subTree.rightChild = self.rightChild
            self.rightChild = subTree
        return subTree

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
        nextPadding = padding + "│  "
        rightPointer = "└──"
        leftPointer = "└──" if node.getRightChild() is None else "├──"
        
        treeBuilder = self.modelTree(nextPadding, leftPointer, node.getLeftChild(), treeBuilder)
        treeBuilder = self.modelTree(nextPadding, rightPointer, node.getRightChild(), treeBuilder)
        
        return treeBuilder

def main():
    rootNode = BinaryTree("root")
    node1 = BinaryTree("node1")
    node2 = BinaryTree("node2")
    node3 = BinaryTree("node3")
    node4 = BinaryTree("node4")
    node5 = BinaryTree("node5")
    node6 = BinaryTree("node6")
    node7 = BinaryTree("node7")
    node8 = BinaryTree("node8")

    rootNode.insertLeft(node1)
    rootNode.insertRight(node2)

    node1.insertLeft(node3)
    node1.insertRight(node4)

    node2.insertLeft(node5)
    node2.insertRight(node6)

    node3.insertLeft(node7)
    node7.insertLeft(node8)

    rootNode.printNodes(rootNode)
    treeBuild = rootNode.modelTree("", "", rootNode)
    
    print("\n\n")
    print(treeBuild)


if __name__ == "__main__":
    main()