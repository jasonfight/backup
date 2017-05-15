#!/usr/bin/python
#coding=utf-8

'''
9. 编写python程序: 实现一个二叉树程序，
封装节点类和方法类。要求至少写出其创建方法和两种遍历方法
（两种遍历方法中要求包含层次遍历，另外一种任选。）
'''
from collections import deque

class TreeNode(object):
    def __init__(self,data = 0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class Bitree(object):
    def __init__(self,root = None):
        self.root = root
    #
    # def is_empty(self):
    #     if self.root is None:
    #         return True
    #     else:
    #         return False

    def preOrder(self,treenode):
        if treenode == None:
            return
        print treenode.data,
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)



    def order(self,treenode):
        if treenode == None:
            return
        queue = deque([treenode])
        while queue:
            node = queue.popleft()
            print node.data,
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        print ""

if __name__ == "__main__":
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1 = TreeNode(1,n3,n4)
    n2 = TreeNode(2,n5,n6)
    root = TreeNode('root',n1,n2)

    bt = Bitree(root)
    print "preorder:"
    bt.preOrder(bt.root)
    print ""
    print "order:"
    bt.order(bt.root)
