# python3
#implementation of "Sliding window full duplex"
#ip = "192.168.43.56" #@ Ritesh 

import socket
import time
from random import *

ip='127.0.0.1'
#ip="192.168.41.130" 

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # main receiver
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # ack sender

s.bind((ip,5056))

#time clause
t=time.time()
t=int(t)
t=t+300


i=0
while True:
	data, addr = s.recvfrom(1024)
	print ("Received from ",addr)
	p=data.decode()
	#print(p)
	p=p.split(' ')
	print(p[1])
	#time.sleep(randint(1,5))

	x=p[0]+ ' ack'
	s1.sendto(x.encode(),(ip,5005))
	
	'''
	if time.time()>t:
		break
	'''	
s.close()
s1.close()
