from os import popen
import queue
from queue import Queue
import threading
from subprocess import Popen,PIPE

class doRun(threading.Thread):                       #继承线程对象
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue
    def run(self):
        while not self._queue.empty():
            ip=self._queue.get()
            # print(ip)
            ping=Popen('ping %s' % ip,shell=True,stdin=PIPE,stdout=PIPE)   #cmd命令对象
            rus=ping.stdout.read().decode('gbk')                            #读取输出并解码为gbk
            if 'TTL' in rus:
                print(ip,'is up')                                           
            else:
                print(ip,'is down')

def main():                                     
    thread=[]                                    #创建线程空列表
    count=10                                     #线程数
    q=Queue()                                    #实例队列
    
    for i in range(1,255):
        q.put('222.138.1.'+str(i))               #put所有ip放入实例队列
    for i in range(count):
        thread.append(doRun(q))                  #实例线程对象加入线程列表  
    for i in thread:  
        i.start()                                   
    for i in thread:  
        i.join()

if __name__ == "__main__":
    main()
