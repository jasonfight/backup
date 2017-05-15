#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None

    def __getitem__(self,key):
        if self.is_empty():
            print "stack is empty"
            return
        else:
            return self.getitem(key)


    def initstack(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length

    def show(self):
        p = self.head.next
        while p != None:
            print p.value,
            p = p.next
        print ""

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = None

    def head_append(self,value):
        # p = self.head
        # Node(value).next = p.next
        # p.next = Node(value)
        p = self.head
        node = Node(value)
        node.next = p.next
        p.next = node

    def pop(self):
        p = self.head
        p.next = p.next.next

    def index(self,value):
        if self.is_empty():
            print "Linklist is empty"
            return
        p = self.head.next
        i = 0
        while p != None and not (p.value == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else:
            return i

    def getitem(self,index):
        if self.is_empty():
            print "link is empty"
            return
        i = 0
        p = self.head.next

        while p != None and i < index:
            i += 1
            p = p.next

        if p == None:
            print "target is noe exist"
        else:
            return p.value
