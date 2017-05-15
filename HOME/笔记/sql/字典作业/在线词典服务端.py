#!/bin/python
#coding=utf-8
import socket,traceback,os,sys,MySQLdb,time

def mian2(c):
    while True:
        data = c.recv(1024)
        global data
        data1 = data.split(' ')
        if data1[0] == "L":
            login(c)
        elif data1[0] == 'R':
            registered(c)
        elif data1[0] == 'Q':
            break

def login(c):
    data1 = data.split(' ')
    # print data1[1]
    # print data1[2]
    cursor.execute('select * from usr where name = "%s" and password = "%s"'%(data1[1],data1[2]))
    results = cursor.fetchall()
    if results == "":
        c.send('no')
        return
    else:
        c.send('OK')
        print '***************************',data1[1]
        query(c)

def registered(c):
    print '..............'
    data1 = data.split(' ')
    try:
        cursor.execute('insert into usr (name,password) values("%s","%s")'%(data1[1],data1[2]))
        db.commit()
    except:
        print 'sfdafsdafsadfsadfsadfds'
        db.rollback()
        c.send('no')
        return

    c.send('OK')
    return

def history(c):
    data1 = data.split(' ')
    cursor.execute('select * from history where name = "%s"'%data1[1])
    jieguo = cursor.fetchall()
    c.send(str(jieguo))

def query(c):
    name = data.split(' ')
    cursor.execute('select * from usr where name = "%s"'%name[1])#执行数据库语句
    result = cursor.fetchall()
    while True:
        f = open('dict.txt','r')
        data1 = c.recv(1024)
        if data1 == '1':
            history(c)
        elif data1 == '2':
            mian2(c)
        elif data1 == '':
            break
        else:
            time1 = time.localtime()
            try:
                cursor.execute('insert into history values("%s","%s","%s-%s-%s %s:%s:%s")'%(result[0][1],data1,time1[0],time1[1],time1[2],time1[3],time1[4],time1[5]))
                db.commit()#如果对数据库造成改变　需要提交　查询不用
            except:
                db.rollback()

            while True:
                x = f.readline()
                m = x.split(' ')

                if data1 == m[0]:
                    del m[0]
                    while m[0] == "":
                        del m[0]
                    translation = ' '.join(m)
                    c.send(translation)
                    break
                if x == "":
                    c.send('查无此词')
                    break

def main():
    while True:
        try:
            c,addr = s.accept()#连接客户端
            print '链接成功'
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue
        pid = os.fork()
        if pid:
            c.close()
            os.waitpid(-1,os.WNOHANG)
            continue
        else:
    	    s.close()
            mian2(c)
    c.close()
    sys.exit(0)

if __name__ == '__main__':
    host = ''
    port = int(sys.argv[1])
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    db = MySQLdb.connect('localhost','root','123','dict')
    cursor = db.cursor()
    main()
