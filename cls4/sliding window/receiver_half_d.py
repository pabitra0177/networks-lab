# python3
import socket
import time
#ip = "192.168.43.56" #@ Ritesh

ip='127.0.0.1'
port = 5089

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))

#time clause
t=time.time()
t=int(t)
t=t+300

while True:
	data, addr = s.recvfrom(1024)
	print ("Received from ",addr)
	p=data.decode()
	print(p)
		
	if time.time()>t:
		break
s.close()
