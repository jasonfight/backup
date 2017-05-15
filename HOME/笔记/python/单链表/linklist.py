#!/usr/bin/python
#coding=utf-8

class Node(object):                   # NOTE: 用来生成结点并传如数据与初始指针
    def __init__(self,val,next=None):
        self.value = val
        self.next = next


class Linklist(object):
    def __init__(self):         # NOTE: 生成头结点,头结点的数据为None
        self.head =None

    def __getitem__(self,key):
        if self.is_empty():
            print "Linklist is empty"
            return
        else:
            return self.getitem(key)

    def __setitem__(self,key,value):
        if key < 0 or key > self.getlength():
            print "The given key is error"
            return
        else:
            self.delete(key)
            return self.insert(key,value)

    def initlist(self,data):
        self.head = Node(0)         # NOTE: 定义头指针,初始化链表,定义头结点
        p = self.head

        for i in data:          # NOTE: 将各个结点链接起来,每一个结点的next 为下一个结点
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):    # NOTE: 返回链表的长度
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length

    def show(self):     # NOTE: 在同一行输出列表的值
        p = self.head.next

        while p != None:
            print p.value,
            p = p.next
        print ""

    def is_empty(self):           # NOTE: 如果链表为空,返回True 如果不为空 返回False
        if self.getlength() == 0:
            return True
        else:
            return False
    def clear(self):                # NOTE: 清空链表,(只需要将头结点变为None即可)
        self.head = None

    def append (self,value):       # NOTE: 在链表后增加一个结点
        p = self.head
        while p != None:
            p = p.next
        p = Node(value)


    def insert (self,index,value):     # NOTE: 在链表特定位置插入一个结点
        if index < 0 or index > self.getlength():
            print "index is error"
            return
        p = self.head
        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1
        q = Node(value)
        q.next = p.next
        p.next = q

    def delete(self,index):    	 # NOTE: 删除一个特定位置的结点
        if self.is_empty() or  index < 0 or index > self.getlength()-1:
            print "index is error"
            return
        p = self.head
        i = 0
        while p.next != None and i < index:
            p =p.next
            i += 1
        if p.next == None:
            print "index is error"
        else:
            p.next = p.next.next

    def index(self,value):      # NOTE: 通过value查找并返回结点的下标
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

    def getitem(self,index):        # NOTE: 通过下标查找并返回结点的值
        if self.is_empty():
            print "link is empty"
            return
        i = 0
        p = self.head.next

        while p != None and i < index:
            i += 1
            p = p.next
        if p == None:
            print "target is not exist"
        else:
            return p.value
