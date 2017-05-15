#!/usr/bin/python
#coding=utf-8

import MySQLdb


def login(act,passwd):
    cursor.execute('select * from usr where account = "%s" and passwd = "%s"'%(act,passwd))
    data = cursor.fetchone()
    if data == None:
        print '账号密码错误,请重新输入'
        exit(1)

    if data[2] == 1:
        teacher()
    if data[2] == 0:
        student(act)

def signin(act,passwd,flag):
    sql = ('insert into usr values("%s","%s",%d)'%(act,passwd,flag))
    try:
        cursor.execute(sql)
        db.commit() #数据提交
        if flag == 1:
            print '注册成功,欢迎您,%s老师:'%act
        else:
            print '注册成功,欢迎您,%s同学:'%act
        print '您的账号为:',act
        print '您的密码为:',passwd
        print '请妥善保管您的密码'
    except:
        db.rollback() #回到执行前的状态
        print 'signin failed'

    # cursor.execute('select * from usr')
    # data = cursor.fetchall()
    # print data
def teacher():
    print '+----------------------welcome-----------------------+'
    print'''|  1) celect(查询) 2) updata(修改)  3) insert(增加)   |'''
    print'''|  4) delete(删除) 5) quit(退出)                      |'''
    print '+----------------------------------------------------+'
    a = raw_input("请输入选项:")
    if  a == '1':
        select()
    if a == '2':
        update()
    if a == '3':
        insert()
    if a == '4':
        delete()
    if a == '5':
        exit(0)
def student(name):
    print '+----------------------welcome---------------------------+'
    print'''|  1) select(查询) 2) chpasswd(修改密码)  3) quit(退出)  |'''
    print '+--------------------------------------------------------+'
    a = raw_input('请输入选项:')
    if a == '1':
        select()
    if a == '2':
        chpasswd(name)
    if a == '3':
        exit(0)

def select():
    name = raw_input('请输入需要查询的姓名:')
    sql=('select * from score where name = "%s"'%name)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        print '该同学不存在,请重新输入!'
    else:
        print '''
查询成功,查询结果为:
        id = %d
        姓名 = %s
        性别 = %s
        分数 = %d
        '''%(data[0],data[1],data[2],data[3])
def update():
    name = raw_input('请输入需要更改的学生姓名:')
    sql=('select * from score where name = "%s"'%name)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        print '该学生不存在!'
        exit()
    new_score = raw_input('请输入新的分数:')
    sql = ('update score set score = %s where name = "%s"'%(new_score,name))
    try:
        cursor.execute(sql)
        db.commit()
        print ' update complete!'
    except:
        dc.rollback()
        print 'update failed!'
def insert():
    name = raw_input('请输入姓名:')
    gender = raw_input('请输入性别:')
    score = raw_input('请输入分数:')
    sql = ('insert into score (name,gender,score) values("%s","%s","%s")'%(name,gender,score))
    try:
        cursor.execute(sql)
        db.commit()
        print 'insert complete!'
    except:
        dc.rollback()
        print 'insert failed!'
def delete():
    name = raw_input("请输入姓名:")
    sql=('select * from score where name = "%s"'%name)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        print '该学生不存在!'
        exit()

    sql=('delete from score where name = "%s"'%name)
    try:
        cursor.execute(sql)
        db.commit()
        print "delete complete!"
    except:
        db.rollback()
        print "delete failed!"


def chpasswd(name):
    old_passwd = raw_input('请输入原密码:')
    sql=('select * from usr where passwd = "%s"'%old_passwd)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        print '密码错误'
        exit(1)
    new_passwd = raw_input('请输入新密码:')
    new_passwd_test = raw_input('请再次输入:')
    if new_passwd != new_passwd_test:
        print '重置密码错误,两次输入的新密码不一致'
        exit()
    else:
        sql = ('update usr set passwd = "%s" where account = "%s"'%(new_passwd,name))
        print name
        try:
            cursor.execute(sql)
            db.commit()
            print 'reset password complete!'
        except:
            db.rollback()
            print "reset password failed"

#打开数据库链接
print '+-------------welcome--------------+'
print'''|  1) login  2) signin  3) quit    |'''
print'''|                                  |'''
print '+----------------------------------+'




if __name__ == '__main__':
    db = MySQLdb.connect('localhost','root','123','student')
    cursor = db.cursor()
    a = raw_input('请输入选项:')

    if a == '1':
        act = raw_input('请输入账号(不能超过10个字符):')
        passwd = raw_input('请输入密码(不能超过10个字符):')
        login(act,passwd)

    elif a == '2':
        act = raw_input('请输入账号(不能超过10个字符):')
        passwd = raw_input('请输入密码(不能超过10个字符):')
        flag = int(raw_input('请输入权限(0或1):'))
        signin(act,passwd,flag)
    elif a == 3 or a == 'q' or a =='quit' or a == 'exit':
        exit(0)


    db.close()
