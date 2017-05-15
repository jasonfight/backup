#!/usr/bin/python
#coding=utf-8
'''
将 2 3 分别传给 N X  
输出:  9
'''
def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
print(f(3))
