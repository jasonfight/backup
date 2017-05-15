#coding=utf-8
import time
import threading
 
#当还剩下一百个产品时，则不进行消费，待生产者生产
#当生产了一千个产品时，则不进行生产，待消费者消费
 
product = 0 #产品初始化时为0
 
lock = threading.Condition()
 
class Producer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)
 
    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product >= 1000:
                    self._lock.wait()
                else:
                    product += 100
                    print "add 100, product count=" + str(product)
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
                    product -= 3
                    print 'consum 3, count=' + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)
 
 
def test():
    for i in range(5):
        p = Producer(lock)
        p.start()
 
    for i in range(5):
        s = Consumer(lock)
        s.start()
 
if __name__ == '__main__':
    test()
