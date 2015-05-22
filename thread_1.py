#coding=utf-8
import threading
from time import ctime,sleep
'''
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})

This constructor should always be called with keyword arguments. Arguments are:

　　group should be None; reserved for future extension when a ThreadGroup class is implemented.

　　target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.

　　name is the thread name. By default, a unique name is constructed of the form “Thread-N” where N is a small decimal number.

　　args is the argument tuple for the target invocation. Defaults to ().

　　kwargs is a dictionary of keyword arguments for the target invocation. Defaults to {}.

If the subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing 

anything else to the thread.

'''

def music(func):
    for i in range(2):
        print " I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print " I was at the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'love',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'avatar',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    #所有子进程结束后，再运行主进程
    print "all over %s" %ctime()