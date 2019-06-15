class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findKnodesDown(root,k):
    if root is None:
        return
    if k is 0:
        print root.data

    findKnodesDown(root.left,k-1)
    findKnodesDown(root.right,k-1)

def findheight(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return 1
    return 1+max(findheight(root.left),findheight(root.right))

root=Node(20)
root.left=Node(8)
root.right=Node(22)
root.left.left=Node(5)
root.left.right=Node(30)
root.right.left=Node(4)
root.right.right=Node(25)
root.left.right.left=Node(10)
root.left.right.right=Node(14)
root.left.right.right.right=Node(17)

k=2
findKnodesDown(root,k)
print "Height:", findheight(root)