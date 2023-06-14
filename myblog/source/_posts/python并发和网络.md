---
title: python并发和网络
date: 2019-04-10 10:31:07
tags: 
    - Python多进程
categories: 
    - Python心得
---
## 进程和线程

- 使用线程来解决I/O限制问题
- 使用进程、网络或事件来处理cpu问题
  标准库中有一个Queue函数。
  
### multiprocessing包
  multiprocessing包是Python中的多进程管理包。与threading.Thread类似，它可以利用multiprocessing.Process对象来创建一个进程。
该进程可以运行在Python程序内部编写的函数。该Process对象与Thread对象的用法相同，也有start(), run(), join()的方法。
此外multiprocessing包中也有Lock/Event/Semaphore/Condition类 (这些对象可以像多线程那样，通过参数传递给各个进程)，用以同步进程，
其用法与threading包中的同名类一致。所以，multiprocessing的很大一部份与threading使用同一套API，只不过换到了多进程的情境。
但在使用这些共享API的时候，我们要注意以下几点:
- 在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。
- multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。
- 多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。
但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率。

  Process.PID中保存有PID，如果进程还没有start()，则PID为None。
  window系统下，需要注意的是要想启动一个子进程，必须加上那句if _ _ name _ _ == "main"，进程相关的要写在这句下面。

#### 简单创建多进程
  有两种使用方法，直接传入要运行的方法或从Process继承并覆盖run()：
  
```python
from multiprocessing import Process
import threading
import time


def foo(i):
    print 'say hi', i

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()

# 方法二

from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg

    def run(self):
        print 'say hi', self.arg
        time.sleep(1)
    
if __name__ == '__main__':

    for i in range(10):
        p = MyProcess(i)
        p.start()


```
#### Process类  
  构造方法：
  def _ _ init _ _ (self, group=None, target=None, name=None, args=(), kwargs={}):
  
  　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 进程名；
　　args/kwargs: 要传入方法的参数。
  注：一般是用 target和args/kwargs
  
  实例方法：
  　is_alive()：返回进程是否在运行。
　　join ( [ timeout ] )：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
　　start()：进程准备就绪，等待CPU调度
　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
　　terminate()：不管任务是否完成，立即停止工作进程
  
  属性：
  　authkey
　　daemon：和线程的setDeamon功能一样
　　exitcode(进程在运行时为None、如果为–N，表示被信号N结束）
　　name：进程名字。
　　pid：进程号。
daemon属性：
- 如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
- 如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
  
  属性daemon的值默认为False，如果需要修改，必须在调用start()方法启动线程之前进行设置。另外要注意的是，
上面的描述并不适用于IDLE环境中的交互模式或脚本运行模式，因为在该环境中的主线程只有在退出Python IDLE时才终止。

## Pool类
  进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。
进程池设置最好等于CPU核心数量

构造方法：
 def Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None):
 Pool( [ processes[, initializer[, initargs[, maxtasksperchild[, context] ]]]])
- processes ：使用的工作进程的数量，如果processes是None那么使用 os.cpu_count()返回的数量。
- initializer： 如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
- maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
- context: 用在制定工作进程启动时的上下文，一般使用 multiprocessing.Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context
实例方法：
　　apply(func[, args[, kwds]])：同步进程池
　　apply_async(func[, args[, kwds[, callback[, error_callback]]]]) ：异步进程池
　　close() ： 关闭进程池，阻止更多的任务提交到pool，待任务完成后，工作进程会退出。
　　terminate() ： 结束工作进程，不在处理未完成的任务
　　join() : wait工作线程的退出，在调用join()前，必须调用close() or terminate()。这样是因为被终止的进程需要被父进程调用wait（join等价与wait），否则进程会成为僵尸进程。pool.join()必须使用在

 
```python
    #例子一（异步进程池）：
#pool.close()或者pool.terminate()之后。其中close()跟terminate()的区别在于close()会等待池中的worker进程执行结束再关闭pool,而terminate()则是直接关闭。
# coding:utf-8
from  multiprocessing import Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100

def Bar(arg):
    print arg

if __name__ == '__main__':
    t_start=time.time()
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)#维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    pool.terminate()
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t
    
    ###例子二（同步进程池）：
    # -*- coding:utf-8 -*-
from  multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(1)
    print i + 100


if __name__ == '__main__':
    t_start=time.time()
    pool = Pool(5)

    for i in range(10):
        pool.apply(Foo, (i,))

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t
    
    ##例子三：异步进程池使用get()方法获得进程执行结果值（错误使用get（）方法获取结果）
def Bar(arg):
    return arg

if __name__ == '__main__':
    t_start=time.time()
    pool = Pool(5)

    for i in range(10):
        res = pool.apply_async(func=Foo, args=(i,), callback=Bar)#维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        print res.get()  ###错误使用get

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    pool.terminate()
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t
    
    ###例子四（正确使用get（）方法获取结果）
    
# coding:utf-8

from  multiprocessing import Pool
import time

def Foo(i):
    time.sleep(2)
    return i + 100

def Bar(arg):
    return arg

if __name__ == '__main__':
    res_list=[]
    t_start=time.time()
    pool = Pool(5)

    for i in range(10):
        res = pool.apply_async(func=Foo, args=(i,), callback=Bar)
        res_list.append(res) ##正确使用get

    pool.close()
    pool.join()
    for res in res_list:
        print res.get()
    t_end=time.time()
    t=t_end-t_start
    print 'the program time is :%s' %t
```
## 进程数据共享
  方法一（使用Array）：
Array(‘i’, range(10))中的‘i’参数C语言中的类型：
‘c’: ctypes.c_char　　　　 ‘u’: ctypes.c_wchar　　　　‘b’: ctypes.c_byte　　　　 ‘B’: ctypes.c_ubyte
‘h’: ctypes.c_short　　　  ‘H’: ctypes.c_ushort　　  ‘i’: ctypes.c_int　　　　　 ‘I’: ctypes.c_uint
‘l’: ctypes.c_long,　　　　‘L’: ctypes.c_ulong　　　　‘f’: ctypes.c_float　　　　‘d’: ctypes.c_double
```python

from multiprocessing import Process, Array

def f(a):
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    arr = Array('i', range(10))
    p = Process(target=f, args=(arr,))
    p.start()
    p.join()

    print(arr[:])

```
  方法二（使用Manager）：
Manager()返回的manager提供list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array类型的支持。

```python
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)

```

## 网络
  IP:本机IP地址一直是：127.0.0.1 ，名称一直为localhost
  
### 套接字
  Python套接字编程教程（  https://docs.python.org/3/howto/sockets.html ）
  
udp-服务器代码：服务器必须用socket包的两个方法来建立网络连接
```python
    from datetime import datetime
    import socket
    
    server_address = ('localhost', 6789)
    max_size = 4096  
    print 'starting the server at',datetime.now()
    print 'waiting for a client to call'
    
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建一个套接字，SOCK_DGRAM表示发送的数据报，表示用UDP
    server.bind(server_address) #绑定套接字
    
    data,client = server.recvfrom(max_size)  #接收数据
    
    print ('At',datetime.now(), client, 'said', data)
    server.sendto(b'Are you talking to me?',client) #发送数据
    server.close()
    
```
UDP-client代码：
```python
    from datetime import datetime
    import socket
    
    server_address = ('localhost', 6789)
    max_size = 4096  
    print 'starting the client at',datetime.now()
    
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建一个套接字，SOCK_DGRAM表示发送的数据报，表示用UDP
    client.sendto(b'hey?',server_address) #发送数据
    
    data,server = client.recvfrom(max_size)  #接收数据
    
    print ('At',datetime.now(), server, 'said', data)
   
    client.close()
    
```

TCP-server代码：
```python
    from datetime import datetime
    import socket
    
    server_address = ('localhost', 6789)
    max_size = 1000  
    
    print 'starting the server at',datetime.now()
    print 'waiting for a client to call'
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个套接字，SOCK_STREAM表示发送的数据报，表示用UDP
    server.bind(server_address) #绑定套接字
    server.listen(5) #监听
    
    client, addr = server.accept()  #接收客户端连接
    data = client.recv(max_size)
    
    
    print ('At',datetime.now(), client, 'said', data)
    client.sendall(b'Are you talking to me?') #发送数据
    
    server.close()
    client.close()
```
TCP-client代码：
```python
    from datetime import datetime
    import socket
    
    address = ('localhost', 6789)
    max_size = 1000  
    print 'starting the client at',datetime.now()
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个套接字，SOCK_STREAM表示发送的数据报，表示用UDP
    client.connect(address)
    client.sendall(b'hey')
    data = client.recv(max_size)

    print ('At',datetime.now(), 'someone said', data) 
    client.close()
    
```
## 远程处理
### 远程调用
  RPC是一种非常流行的技术，有很多种实现方式。标准库中包含一种RPC实现，xmlrpc，使用XML作为传输格式。在服务器上定义并注册函数，。
客户端使用类似导入方式来调用它们。
xmlr_server.py

```python
    from xmlrpc.server import SimpleXMLRPCServer
    """
    在服务器上提供了double()函数，注册函数后，才能通过RPC调用
    
    """
    def double(num):
        return num*2
    server = simpleXMLRPCServer(("localhost",6789))
    server.register_function(double,"double")#注册函数
    server.serve_forever()
   
```

xmlr_client.py

```python
    from xmlrpc.client
    """
    客户端通过ServerProxy()和服务器连接。接着会调用proxy.double()
    
    """
    
    proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
    num = 7
    result = proxy.double(num)
    print('Double %s is %s ' %(num,result))
    

```
#### 使用msgpack-rpc-python
  安装：pip install msgpack-rpc-python
  server代码：msgpack_server.py

```python
    from msgpackrpc import Server, Address
    
    class Services():
        def double(self, num):
            return num *2
    
    
    server = Server(Services())
    server.listen(Address('localhost',6789))
    server.start()

```
  client代码 :msgpack_client.py
  
```python
    from msgpackrpc import Client, Address
    
    client = Client(Address('localhost',6789))
    num = 8
    result = client.call('double',num)
    print("Double %s is %s " %(num, result))

```
  
#### 使用fabric

    fabric包可以运行远程或者本地命令、上传或下载文件、用sudo权限运行命令。
     pip2 install fabric
fab1.py
```python
    def iso():
        from datetime import date
        print(date.today().isoformat())
        

```
输入以下命令执行：
fab -f fabl.py -H localhost iso

其中：-f fab1.py选项指定使用fabric文件执行fab1.py。-H localhosh选项指定运行本地的命令，最后的iso是fab文件中要运行的函数名。

     



