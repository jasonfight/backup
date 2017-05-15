#!/usr/bin/python
#coding=utf-8
from collections import deque
class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class Bittree(object):
    def __init__(self,root = None):
        self.root = root

    def preOrder(self,treenode):
        if treenode == None:
            return
        print treenode.data
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)


    def inOrder(self,treenode):
        if treenode == None:
            return
        self.inOrder(treenode.left)
        print treenode.data
        self.inOrder(treenode.right)

    def postOrder(self,treenode):
        if treenode == None:
            return
        self.postOrder(treenode.left)
        self.postOrder(treenode.right)
        print treenode.data

    def Order(self,treenode):
        if treenode == None:
            return
        queue = deque([treenode])
        while queue:
            node = queue.popleft()
            print node.data
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2,n1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5,n3,n4)
    n6 = TreeNode(6,n2,n5)
    n7 = TreeNode(7,n6)
    n8 = TreeNode(8)
    root = TreeNode("root",n7,n8)
    bt = Bittree(root)
    print "先序遍历"
    bt.preOrder(bt.root)
    print "中序遍历"
    bt.inOrder(bt.root)
    print "后序遍历"
    bt.postOrder(bt.root)

    bt.Order(bt.root)
