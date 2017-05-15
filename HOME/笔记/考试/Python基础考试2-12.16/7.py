#!/usr/bin/python
#coding=utf-8
'''
7 编写python程序: 完成逆波兰表达式，要求用栈的方式完成，
完成效果类似于终端的dc命令。以‘p’作为输入的结束。
支持“+ - * /”四个运算即可。为降低难度你也可以只实现个位数的运算。
'''
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
    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length
    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False
    def initstack(self,data):
        self.head = Node(0)
        p = self.head
        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def show(self):
        p = self.head.next
        while p != None:
            print p.value,
            p = p.next
        print ""
    def head_append(self,value):
        p = self.head
        node = Node(value)
        node.next = p.next
        p.next = node
    def pop(self):
        p = self.head
        p.next = p.next.next

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

s=Stack()
s.initstack([])

a=raw_input('请输入逆波澜计算式:')
if a[len(a)-1] != "p":
    print "逆波澜表达式应以p结尾."
    exit()
for i in a:
    if i =="p":
        break
    s.head_append(i)
    if i in ['+','-','*',"/"]:
        if i == "+":
            result = int(s[2]) + int(s[1])
        elif  i == "-":
            result = int(s[2]) - int(s[1])
        elif i == "*":
            result = int(s[2]) * int(s[1])
        elif i == "/":
            result = int(s[2]) / int(s[1])
        s.pop()
        s.pop()
        s.pop()
        s.head_append(result)
print "结果是:",result
