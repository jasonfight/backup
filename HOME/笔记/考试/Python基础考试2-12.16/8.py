#!/usr/bin/python
#coding=utf-8

'''
8. 编写python程序: 使用链式存储的方法完成一个链式队列。
要求最少实现队列创建，入队，出队，清空队列四个方法。并进行封装。
'''

class Node(object):                   # NOTE: 用来生成结点并传如数据与初始指针
    def __init__(self,val,next=None):
        self.value = val
        self.next = next


class Deque(object):
    def __init__(self):
        self.head =None
    def initdeque(self,data):
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

    def append (self,value):
        p = self.head
        node = Node(value)
        node.next = p.next
        p.next = node


    def pop(self):
        if self.is_empty():
            print "index is error"
            return
        p = self.head
        i = 0
        while p.next.next != None :
            p =p.next
            i += 1
        p.next = p.next.next


if __name__ == "__main__":
    queue = Deque()
    queue.initdeque([1,2,3,4,5])

    queue.show()

    queue.append(10)
    queue.show()

    queue.pop()
    queue.show()
    queue.pop()
    queue.show()
