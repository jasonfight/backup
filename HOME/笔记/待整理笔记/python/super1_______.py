#!/usr/bin/python
#coding=utf-8
__metaclass__ = type

class Bird1:
    def __init__(self):
        self.hungry = True
        self.call = "gugugu1"
    def eat(self):
        if self.hungry:
            print "Aaaah......"
            self.hungry = False
        else:
            print "No Thanks..."
class Bird2:
    def __init__(self):
        self.call = "gugugu2"
    def talk(self):
        print self.call


class SongBird(Bird1,Bird2):
    def __init__(self):
        super(SongBird,self).__init__()

    def eat(self):
        print "songbird eat...."
    def talk(self):
        print "songbird talk...."

if __name__ == "__main__":

    niao = SongBird()
    niao.eat()
    niao.eat()
    niao.talk()

    super(SongBird,niao).eat()
    super(SongBird,niao).eat()
    super(SongBird,niao).talk() # NOTE:
    '''
    在Bird1中的 __init__ 中添加了 call属性, 该语句就可执行,why?????
    并且继承Bird1的属性的同时,继承Bird2的方法
    '''
