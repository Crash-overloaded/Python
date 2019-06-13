#!/usr/bin/python3
data=input("Enter a paragraph:-")
new_data=data[0:500]
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in chars:
        c=new_data.count(i)
        if c > 1:
                print("    Characters:-     No. of times repeated:-")
                print("                "+str(i),"                       "+str(c))

words=new_data.split(" ")
c=[words.count(i) for i in words]
a=dict(zip(words,c))
'''
for i in a:
	if a[i] > 1:
		data=[i,a[i]]
		print(data)
'''

for i in list(a):
	if a[i] > 5:
		del [a[i]]
	elif a[i] > 1:
		data=[i,a[i]]
		print(data)
		
			

		

