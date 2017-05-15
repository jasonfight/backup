#!/usr/bin/python

import os

print os.listdir('.')
print '1:',os.path.isdir('test')
print '2:',os.path.isfile('test')

file_path = os.path.join('home/linux','test','test.txt')

print file_path

filename = raw_input('file name:')

os.stat(filename)


#os.system('ls -l')
