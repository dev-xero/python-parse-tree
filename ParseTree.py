# --------------------------------------------------------------------

from BinaryTree import BinaryTree

# --------------------------------------------------------------------

def buildParseTree(fpexp: str):
    fplist = fpexp.split()
    pStack: [BinaryTree] = []
    eTree = BinaryTree("")

    pStack.insert(0, eTree)
    currTree = eTree

    for i in fplist:
        if i == "(":
            currTree.insertLeft(BinaryTree(''))
            pStack.insert(0, currTree)
            currTree = currTree.getLeftChild()
        
        elif i in ['+', '-', '/', '*']:
            currTree.setRootKey(i)
            currTree.insertRight(BinaryTree(i))
            pStack.insert(0, currTree)
            currTree = currTree.getRightChild()
        
        elif i == ')':
            pStack.pop()
        
        elif i != ['+', '-', '/', '*']:
            try:
                currTree.setRootKey(int(i))
                parent = pStack.pop()
                currTree = parent
            
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))
    
    return eTree

