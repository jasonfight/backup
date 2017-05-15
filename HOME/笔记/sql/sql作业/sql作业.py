#!/usr/bin/python
#coding=utf-8

import MySQLdb


def login():
    n = 0
    while n == 0:
        account = raw_input('请输入账号(不能超过10个字符):')
        passwd = raw_input('请输入密码(不能超过10个字符):')
        cursor.execute('select * from usr where account = "%s" and passwd = "%s"'%(account,passwd))
        data = cursor.fetchone()
        if data == None:
            print '账号密码错误,请重新输入!'
            continue

        if data[2] == 1:
            teacher(account)
            n = 1
        if data[2] == 0:
            student(account)
            n = 1
def signin():
    account = raw_input('请输入账号(不能超过15个字符):')
    passwd = raw_input('请输入密码(不能超过10个字符):')

    n = 0
    while n == 0:
        flag = int(raw_input('请输入您的职业(0代表学生,1代表老师):'))
        if flag != 0 and flag  !=1 :
            print '输入错误,请重新输入(0代表学生,1代表老师)'
            continue
        n = 1
    sql = ('insert into usr values("%s","%s",%d)'%(account,passwd,flag))
    try:
        cursor.execute(sql)
        db.commit() #数据提交
    except:
        db.rollback() #回到执行前的状态
        print '注册失败!'
        exit()
    if flag == 1:
        print '注册成功,欢迎您,%s老师:'%account
    else:
        print '注册成功,欢迎您,%s同学:'%account
    print '您的账号为:',account
    print '您的密码为:',passwd
    print '请妥善保管您的账号密码'

def teacher(name):
    print '+----------------------welcome-----------------------+'
    print'''|  1) select(查询) 2) update(修改)  3) insert(增加)   |'''
    print'''|  4) delete(删除) 5) quit(退出)    6) back(重新登录) |'''
    print '+----------------------------------------------------+'
    n = 0
    while n == 0:
        a = raw_input("欢迎%s老师,请输入选项:"%name)
        if  a == '1':
            select(1,name)
            n=1
        elif a == '2':
            update(name)
            n=1
        elif a == '3':
            insert(name)
            n=1
        elif a == '4':
            delete(name)
            n=1
        elif a == '5':
            print '退出成功,再见~'
            exit(0)
        elif a == '6':
            print "退出登录成功,请重新登录!"
            login()
        else:
            print '输入错误,请重新输入!'
            continue
def student(name):
    print '+---------------welcome---------------------+'
    print'''|  1) select(查询) 2) resetpasswd(修改密码) |'''
    print'''|  3) quit(退出)   4) back(重新登录)        |'''
    print '+-------------------------------------------+'
    n = 0
    while n == 0:
        a = raw_input('欢迎%s同学,请输入选项:'%name)
        if a == '1':
            select(0,name)
            n=1
        elif a == '2':
            resetpasswd(name)
            n=1
        elif a == '3':
            print '退出成功,再见~'
            exit(0)
        elif a == '4':
            print '退出登录成功,请重新登录!'
            login()
        else:
            print "输入错误,请重新输入!"
            continue
def select(flag,name):
    n = 0
    while n == 0:
        name_search = raw_input('请输入需要查询的姓名:')
        sql=('select * from score where name = "%s"'%name_search)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data == None:
            print '该同学不存在,请重新输入!'
            continue
        else:
            print '''
    查询成功,查询结果为:
            id   = %d
            姓名 = %s
            性别 = %s
            分数 = %d
            '''%(data[0],data[1],data[2],data[3])
        m = 0
        while m == 0:

            a = raw_input('''是否继续查询? 1)继续  2)退出  3)返回\n''')
            if a == '1':
                select(flag,name)
                m = 1
            elif a == '2':
                print '退出成功,再见~'
                exit(0)
            elif a == '3':
                if flag == 0:
                    student(name)
                    exit(0)
                elif flag == 1:
                    teacher(name)
                    exit(0)
            else:
                print "输入错误,请重新输入!"
                continue

def update(account):
    n = 0
    while n == 0:
        name = raw_input('请输入需要更改的学生姓名:')
        sql=('select * from score where name = "%s"'%name)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data == None:
            print '该学生不存在!,请重新输入'
            continue
        n = 1
    n = 0
    while n == 0:
        new_score = raw_input('请输入新的成绩:')
        if int(new_score) < 0 or int(new_score) > 100:
            print '输入错误,请重新输入成绩'
            continue
        n = 1
    sql = ('update score set score = %s where name = "%s"'%(new_score,name))
    try:
        cursor.execute(sql)
        db.commit()
        print '成绩更新完成'
    except:
        dc.rollback()
        print '成绩更新失败'
    n = 0
    while n == 0:
        a = raw_input('''是否继续更新? 1)继续更新  2)退出程序 3)返回 ''')
        if a == '1':
            update(account)
            n =1
        elif a == '2':
            print '退出成功!再见~'
            exit(0)
        elif a == '3':
            teacher(account)
        else:
            print '输入错误,请重新输入!'
            continue

def insert(account):
    name = raw_input('请输入姓名:')
    n = 0
    while n == 0:
        gender = raw_input('请输入性别(male或者female):')
        if gender == 'male' or gender == 'female':
            n = 1
        else:
            print '输入错误,请重新输入性别(male或female):'
            continue
    n = 0
    while n == 0:
        score = raw_input('请输入成绩(0~100):')
        if int(score) < 0 or int(score) > 100:
            print '输入错误,请重新输入成绩(0~100)'
            continue
        n = 1

    sql = ('insert into score (name,gender,score) values("%s","%s","%s")'%(name,gender,score))
    try:
        cursor.execute(sql)
        db.commit()
        print '创建新同学信息成功'
    except:
        dc.rollback()
        print '创建新同学信息失败'
    n = 0
    while n == 0:
        a = raw_input('''是否继续创建? 1)继续创建  2)退出程序 3)返回 ''')
        if a == '1':
            insert(account)
            n =1
        elif a == '2':
            print '退出成功!再见~'
            exit(0)
        elif a == '3':
            teacher(account)

def delete(account):
    n = 0
    while n == 0:
        name = raw_input("请输入姓名:")
        sql=('select * from score where name = "%s"'%name)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data == None:
            print '该学生不存在!请重新输入'
            continue
        n = 1
    sql=('delete from score where name = "%s"'%name)
    try:
        cursor.execute(sql)
        db.commit()
        print "删除学生信息成功!"
    except:
        db.rollback()
        print "删除学生信息失败!"
        delete()
        exit(0)
    n = 0
    while n == 0:
        a = raw_input('''是否继续删除? 1)继续删除  2)退出程序 3)返回 ''')
        if a == '1':
            delete(account)
            n =1
        elif a == '2':
            print '退出成功!再见~'
            exit(0)
        elif a == '3':
            teacher(account)
        else:
            print '输入错误,请重新输入!'
            continue



def resetpasswd(account):
    n = 0
    while n < 4:
        old_passwd = raw_input('请输入原密码:')
        sql=('select * from usr where passwd = "%s" and account = "%s"'%(old_passwd,account) )
        cursor.execute(sql)
        data = cursor.fetchone()
        if data == None:
            if n == 2:
                print '密码验证失败,结束程序!'
                exit(1)
            print '密码错误,请重新输入,剩余%d次机会'%(2-n)
            n+=1
            continue
        else:
            print '密码验证成功!'
            break
    n = 0
    while n == 0:
        new_passwd = raw_input('请输入新密码(长度不能超过10个字符):')
        if len(new_passwd) > 10:
            print '输入错误,密码长度不能超过10个字符'
            continue
        new_passwd_test = raw_input('请再次输入:')
        if new_passwd != new_passwd_test:
            print '重置密码错误,两次输入的新密码不一致,请重新输入!'
            continue
        n = 1
    sql = ('update usr set passwd = "%s" where account = "%s"'%(new_passwd,account))
    try:
        cursor.execute(sql)
        db.commit()
        print '修改密码成功!'
    except:
        db.rollback()
        print "修改密码失败!"

db = MySQLdb.connect('localhost','root','123','student')
cursor = db.cursor()



if __name__ == '__main__':

    print '+-------------welcome--------------+'
    print'''|  1) login  2) signin  3) quit    |'''
    print'''|                                  |'''
    print '+----------------------------------+'

    n = 0
    while n == 0 :
        a = raw_input('请输入选项:')
        if a == '1':login();n = 1
        elif a == '2':signin();n = 1
        elif a == '3' or a == 'q' or a =='quit' or a == 'exit':
            exit(0)
            n = 1
        else:
            print '输入错误,请重新输入:'
            continue
    db.close()
