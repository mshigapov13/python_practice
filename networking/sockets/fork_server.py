import os, time, sys
from socket import *


myHost = ''
myPort = 9090
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)


def now():
    return time.ctime(time.time())


active_Children = []


def reap_Cheldren():
    while active_Children:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        active_Children.remove(pid)


def handle_Client(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end='')
        print('at', now())
        reap_Cheldren()
        child_Pid = os.fork()
        if child_Pid == 0:
            handle_Client(connection)
        else:
            active_Children.append(child_Pid)


dispatcher()