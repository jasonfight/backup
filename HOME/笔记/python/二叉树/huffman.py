#!/usr/bin/python

class Node(object):
    def __init__(self,weight = 0,left = None,right = None):
        self.weight = weight
        self.left = left
        self.right = right

def  sort(list):
    return sorted(list,key = lambda node:node.weight)

def huffman(list):
    while len(list) != 1:
        a,b = list[0],list[1]
        new = Node()
        new.weight = a.weight + b.weight
        new.left,new.right = a,b
        list.remove(a)
        list.remove(b)
        list.append(new)
        list = sort(list)
    return list

def preOrder(treenode):
    if treenode == None:
        return
    print treenode.weight
    preOrder(treenode.left)
    preOrder(treenode.right)

def get_height(node):
    if node.left == None and node.right == None:
        return 1
    return get_height(node.left) + get_height(node.right)

list = []

for i in range(1,5):
    w = input('The weight:')
    list.append(Node(w))
list = sort(list)

head = huffman(list)[0]

preOrder(head)

print  get_height(head)
