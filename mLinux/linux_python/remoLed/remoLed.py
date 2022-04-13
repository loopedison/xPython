import socket
import time

g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def init(ip, port):
    g_sock.connect((ip, port))
    time.sleep(2)
    return

def send(data):
    g_sock.send(data)
    return

def read():
    data = g_sock.recv(1024)
    return data

def end():
    g_sock.close()
    return

def _test(ip, port):
    sock = init(ip, port)
    send("I am Raspberry Pi\r\n!");
    print read(1024);
    sock.close()
    return

if __name__=='__main__':
    #_test('192.168.2.1', 9999)
    import sys
    if len(sys.argv) == 3:
        _test(sys.argv[1], int(sys.argv[2]))
    else:
        print 'usage:'+sys.argv[0]+' ip  port\r\n'
