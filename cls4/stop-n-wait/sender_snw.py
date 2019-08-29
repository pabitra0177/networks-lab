# python3
#implementation of "STOP-n-WAIT"

import socket
import time

#ip = "192.168.43.56"

# for self comm 2 terminal
ip='127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # main sender
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # ack receiver

s1.bind((ip,8051))
i=0
for i in range(100):
	x=input()
	s.sendto(x.encode(),(ip,8056))
	
	data, addr = s1.recvfrom(1024)
	print ("Received from ",addr)
	p=data.decode()
	print(p)    
    
s.close()
s1.close()
