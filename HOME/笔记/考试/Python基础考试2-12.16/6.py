#!/usr/bin/python
#coding=utf-8

'''
6. 编写python程序: 实现一个双向循环链表，封装结点和其他方法。
要求至少实现创建和增删方法，并且要求实现其__getitem__和__setitem__两个魔法方法。
（如果你的__setitem__即可实现链表的插入那么可以不必写额外的插入方法）
'''

class Node(object):
    def __init__(self,value,prior=None,next=None):
        self.value = value
        self.prior = prior
        self.next = next

class Linklist(object):
    def __init__(self,):
        self.head = None
    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data :
            node = Node(i)
            p.next = node
            node.prior = p
            p = p.next
        p.next = self.head
        self.head.prior = p

    def show(self):
        p =self.head.next
        while p !=self.head:
            print p.value,
            p = p.next
        print ""

    def insert(self,index,value):
        p = self.head
        i = 0
        while p.next != self.head and i < index:
            i += 1
            p = p.next
        q = Node(value)
        p.next.prior = q
        q.next = p.next
        p.next = q
        q.prior =p


    def delete(self,index):
        p =self.head
        i = 0
        while p.next != self.head and i< index:
            p =p.next
            i += 1
        p.next = p.next.next
        p.next.prior = p
    def is_empty(self):
        if self.head == None:
            print "空列表"
            return True
        else:
            return False


    def getitem(self,index):
        p = self.head.next
        i = 0
        while p != self.head and i < index:
            p = p.next
            i += 1
            return p.value


    def __getitem__(self,index):
        if self.is_empty():
            print "Linklist is empty"
            return
        else:
            p = self.head.next
            i = 0
            while p != self.head and i < index:
                p = p.next
                i += 1
            return p.value
    def __setitem__(self,index,value):
        self.delete(index)
        return self.insert(index,value)



if __name__ == "__main__":

    l = Linklist()
    print "创建一个双链表:"
    l.initlist([1,2,3,5,3,6,8])
    l.show()
    print '删除下标为2的结点:'
    l.delete(2)
    l.show()

    print "使用魔法方法__getitem__列出下标为1的结点:",l[1]
    l.show()
    print "使用魔法方法__setitm__修改链表:"
    l[1] = 10
    l.show()
