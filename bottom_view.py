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
def findBottomView(root):
    if root==None:
        return
    hd=0
    root.hd=hd
    #initialise a dictionary to store <hd,node_with_hd>
    
    hd_dict={}

    q=deque()
    #adding root to queue
    q.append(root)
    while q:
        #while queue is not empty , delete nodes fom left one by one and update hd as current node's hd.This will help in setting the hd for left and right child
        temp=q.popleft()
        hd=temp.hd
        #if presnt in hd_dict, the get the value , else make the key and set the value to 0.
        hd_dict[hd]=hd_dict.get(hd,0)
    
        #always update the last node traversed on a horizontal distance
        
        hd_dict[hd]=temp.data
        # if left node exists, set it's hd to its root hd-1 and append it to q
        if temp.left!=None:
            q.append(temp.left)
            temp.left.hd=temp.hd-1
        # if right node exists, set it's hd to its root hd+1 and append it to q
        if temp.right!=None:
            q.append(temp.right)
            temp.right.hd=temp.hd+1
    #print all the values in dictionary values.
    result=hd_dict.values()
    print ' '.join(str(x) for x in result)
root=Node(20)
root.left=Node(8)
root.right=Node(22)
root.left.left=Node(5)
root.left.right=Node(30)
root.right.left=Node(4)
root.right.right=Node(25)
root.left.right.left=Node(10)
root.left.right.right=Node(14)
print "Bottom view of the tree is "
findBottomView(root)
