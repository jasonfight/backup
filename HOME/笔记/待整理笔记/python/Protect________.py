#!/usr/bin/python

class Protect:
    def __init__(self):
        self.job = 'teacher'
        self.__name = 'cainiao'

    @property
    def name(self):
        return self.__name

    def __python(self):
        print('I love python')

    def code(self):
        print("Which language do you like")
        self.__python()
    @property
    def python(self):
        return self.__python

if __name__ == '__main__':
    p = Protect()
    print(p.job)
    print(p.name)
    p.code()
    p.python()
