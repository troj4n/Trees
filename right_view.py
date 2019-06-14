# coding: utf-8
# Your code here!
from collections import deque

#initialise node 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hd=None
def rightviewUtil(root,level,max_level):
    if root==None:
        return
    if max_level[0]<level:
        max_level[0]=level
        print "%d" %(root.data)
    rightviewUtil(root.right,level+1,max_level)
    rightviewUtil(root.left,level+1,max_level)
def findRightView(root):
    max_level=[0]
    rightviewUtil(root,1,max_level)
root=Node(20)
root.left=Node(8)
root.right=Node(22)
root.left.left=Node(5)
root.left.right=Node(30)
root.right.left=Node(4)
root.right.right=Node(25)
root.left.right.left=Node(10)
root.left.right.right=Node(14)
print "Right view of the tree is "
findRightView(root)
