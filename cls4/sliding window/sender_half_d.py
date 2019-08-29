# python3
#half_duplex
import socket
#ip = "192.168.43.56"

def chunkstring(string, length):
	return (string[0+i:length+i] for i in range(0, len(string), length))

ip='127.0.0.1'
port = 5089

print('Enter the data')
input_string=input()
print("Enter the window size ")
k=int(input())

lis=list(chunkstring(input_string,k))
print(lis)
l=len(lis)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(0,l,2):
    x=lis[i]+"  "+lis[i+1]
    s.sendto(x.encode(),(ip,port))

s.close()
