#!/usr/bin/python
#coding=utf-8
'''
8. 使用多线程完成生产者消费者模式编码，资源控制使用线程锁完成
'''
import time,threading
product = 0
lock = threading.Condition()

class Producer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product >= 100:
                    self._lock.wait()
                else:
                    product += 10
                    print "生产10个, 总数=" + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product < 100:
                    self._lock.wait()
                else:
                    product -= 15
                    print '消费15个,总数=' + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)


def test():
    for i in range(2):
        p = Producer(lock)
        p.start()

    for i in range(2):
        s = Consumer(lock)
        s.start()

if __name__ == '__main__':
    test()
