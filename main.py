# ------------------------------------------------------------------

from BinaryTree import BinaryTree as Bt
from ParseTree import buildParseTree

# -----------------------------------------------------------------

def main():
    rootNode = Bt("root")
    node1 = Bt("node1")
    node2 = Bt("node2")
    node3 = Bt("node3")
    node4 = Bt("node4")
    node5 = Bt("node5")
    node6 = Bt("node6")
    node7 = Bt("node7")
    node8 = Bt("node8")

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

    pt = buildParseTree("( 3 + 5 ) * ( 7 - 2 )")
    rootNode.printNodes(pt)


if __name__ == "__main__":
    main()