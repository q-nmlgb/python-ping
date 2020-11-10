from os import popen
import queue
from queue import Queue
import threading
from subprocess import Popen,PIPE

class doRun(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue
    def run(self):
        while not self._queue.empty():
            ip=self._queue.get()
            # print(ip)
            ping=Popen('ping %s' % ip,shell=True,stdin=PIPE,stdout=PIPE)
            rus=ping.stdout.read().decode('gbk')
            if 'TTL' in rus:
                print(ip,'is up')
            else:
                print(ip,'is down')

def main():
    thread=[]
    count=10
    q=Queue()
    
    for i in range(1,255):
        q.put('222.138.1.'+str(i))
    for i in range(count):
        thread.append(doRun(q))  
    for i in thread:  
        i.start()
    for i in thread:  
        i.join()

if __name__ == "__main__":
    main()
