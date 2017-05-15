#!/usr/bin/python
#coding=utf-8
#静态方法和类方法看似没什么差别，但是下面的行为体现了类方法的作用

class Color(object):
    _color = (0, 0, 0);

    @classmethod
    def value(cls):
        if cls.__name__== 'Red':
            cls._color  = (255, 0, 0)
        elif cls.__name__ == 'Green':
            cls._color = (0, 255, 0)
        return cls._color

class Red(Color):
    pass

class Green(Color):
    pass

class UnknownColor(Color):
    pass

red = Red()
green =Green()
xcolor =UnknownColor()

print 'red =',red.value()
print 'green= ',green.value()
print 'xcolor=',xcolor.value()
