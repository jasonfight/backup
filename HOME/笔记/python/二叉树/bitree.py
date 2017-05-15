#!/usr/bin/python
from collections import deque

class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class Bitree(object):
    def __init__(self,root = None):
        self.root = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

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

    def order(self,treenode):
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
    root = TreeNode('root',n7,n8)

    bt = Bitree(root)
    print "preorder...."
    bt.preOrder(bt.root)
    print "inorder...."
    bt.inOrder(bt.root)
    print "postorder...."
    bt.postOrder(bt.root)
    print "order...."
    bt.order(bt.root)
