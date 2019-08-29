# python3
#implementation of "Sliding window full duplex"

import socket
import time

def chunkstring(string, length):
	return (string[0+i:length+i] for i in range(0, len(string), length))

# for self comm 2 terminal
ip='127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # main sender
s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # ack receiver

s1.bind((ip,5005))

print('Enter the data')
input_string=input()
#print("Enter the window size ")
#k=int(input())
k=4
#input_string=input_string*10 ## making it bigger 

lis=list(chunkstring(input_string,k))
print(lis)
l=len(lis)

for i in range(0,l,k):
	
	for j in range(i,i+k):
		if j>=l:
			break
		base=j-i
		base=bin(base).replace('0b','')+' '
		x=base+lis[j]
		s.sendto(x.encode(),(ip,5056))
	
	for k in range(0,k):
		data, addr = s1.recvfrom(1024)
		print ("Received from ",addr)
		p=data.decode()
		print(p)    
    
s.close()
s1.close()
