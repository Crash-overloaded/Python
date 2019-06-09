#!/usr/bin/python3
numbers=[1,2,3,1,4,5,66,22,2,6,0,9]
greater=[]
lesser=[]
for i in numbers:
	if i > 5:
		greater.append(i)
	elif i <= 2:
		lesser.append(i)
print("No. greater than 5:-"+str(greater))
print("No. less than or eq to 2:-"+str(lesser))
