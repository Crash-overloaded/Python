#!/usr/bin/python3
import datetime
name=input("Enter your name:-")
datetime=datetime.datetime.now()
time=datetime.hour
if time>=5 and  time<12:
	print("Good Morning"+str(name))

elif time>=12 and  time<17:
	print("Good Afternoon"+str(name))

elif time>=17 and  time<20:
	print("Good Evening"+str(name))
	
elif time>=20 and time<5:
	print("Good Night"+str(name))

