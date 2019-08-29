# python3
#implementation of "STOP-n-WAIT"
#ip = "192.168.43.56" #@ Ritesh 

import socket
import time
from random import *

# for self comm 2 terminal
ip='127.0.0.1'

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # main receiver
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # ack sender

s.bind((ip,8056))

#time clause
t=time.time()
t=int(t)
t=t+300

i=0
for i in range(100):
	data, addr = s.recvfrom(1024)
	print ("Received from ",addr)
	p=data.decode()
	print(p)
	time.sleep(randint(1,3))
		
	x='ack'
	s1.sendto(x.encode(),(ip,8051))
		
	if time.time()>t:
		break

s.close()
s1.close()
