#!/usr/bin/python
#coding=Utf-8
'''
5. 编写python程序: 实现一个单链表。要求封装链表结点和链表创建及增删改查方法。
'''



class Node(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class Linklist(object):
    def __init__(self):
        self.head = None
    def initlist(self,data):
        self.head = Node(0)
        p = self.head
        for i in data:
            p.next = Node(i)
            p =p.next
    def show(self):
        p = self.head
        while p.next != None:
            print p.next.value,
            p = p.next
        print ""

    def getlength(self):
        length = 0
        p = self.head
        while p.next != None:
            length+=1
            p=p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False
    def append(self,value):
        p = self.head
        while p.next != None:
            p =p.next
        p.next = Node(value)

    def delete(self,index):
        p = self.head
        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1
        p.next = p.next.next
    def setitem(self,index,value):
        p = self.head
        node = Node(value)
        i = 0
        while p.next != None  and i < index:
            p = p.next
            i += 1
        node.next = p.next
        p.next = node

    def getitem(self,index):
            p = self.head
            i = 0
            while p.next != None and i < index:
                p = p.next
                i += 1
            print p.next.value

if __name__=="__main__":
    l=Linklist()
    l.initlist([1,2,3,5,6])
    print "原始链表:"
    l.show()
    print "链表长度为:",l.getlength()
    print "链表的增加:"
    l.append(10)
    l.show()
    print "链表的删除:"
    l.delete(0)
    l.show()
    print "链表的更改:"
    l.setitem(2,19)
    l.show()
    print "查找下标为0的项:"

    l.getitem(0)
