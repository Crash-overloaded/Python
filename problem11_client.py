#!/usr/bin/python2

import socket 
print  '''
		Welcome !!!
		Type 'quit' to exit chat!


	'''
server_ip=raw_input("Enter your IP address:-")
server_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((server_ip,server_port))
while True:
	data=s.recvfrom(100)
	if data[0] == "Server left the chat!":
		print data[0]
		s.close()	
		break
	else:
		print "Message from server:-"+data[0]
		user=raw_input("Enter message:-")
		if user=="quit":
			a="Client left the chat!"
			s.sendto(str(a),data[1])
			s.close()
			break
		else:
			if len(user) > 150:
				print "Error:-Limit of characters exceeded 150!!"
			else:
				s.sendto(str(user),data[1])
s.close()
