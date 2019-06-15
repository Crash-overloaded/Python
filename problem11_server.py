#!/usr/bin/python2

import socket

print   """
		Welcome to chat room!!!
		Type 'quit' to exit the chat!


	"""
rec_ip=raw_input("Enter client IP address:-")
rec_port=5346
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind((rec_ip,rec_port))
while True:
	user=raw_input("Enter message:-")
	if user=="quit":
		a="Server left the chat!"
		s.sendto(str(a),(rec_ip,rec_port))
		s.close()
		break
	else:
		if len(user) > 150:
			print "Error:-More than 150 words typed!!"	
		else:
			s.sendto(str(user),(rec_ip,rec_port))
			data=s.recvfrom(100)
			if data[0]=="Client left the chat!":
				print data[0]
				s.close()
				break
			else:
				print "Message from client:-"+data[0]
			
s.close()
