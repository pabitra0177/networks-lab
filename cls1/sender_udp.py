# python3
import socket

ip = "192.168.43.56"
port = 5001
i=0
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(100):
    x=input()
    s.sendto(x.encode(),(ip,port))

s.close()
