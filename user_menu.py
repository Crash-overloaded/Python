#!/usr/bin/python3

import os
choice="""
press 1  to OPEN CALC.
press 2  to OPEN Text Editor.
press 3  to Create Directory.
press 4  to Reboot Your Machine.
press 5  to CHECK CURRENT RAM USED out of Total.
press 6 to exit.
"""
while True:
	print(choice)
	ch=int(input("Enter choice:-"))

	if ch==1:
		os.system("gnome-calculator &>/dev/null")
		os.system("clear")
	elif ch==2:
		os.system("gedit")
		os.system("clear")
	elif ch==3:
		name=input("Enter directory name:-")
		os.mkdir(name)
		os.system("clear")
	elif ch==4:
		reboot=input("Are you sure you want to reboot(y/n):-")
		if reboot=="y":
			os.system("Reboot")
		elif reboot=="n":
			print("Not rebooting...")
			os.system("clear")
	elif ch==5:
		os.system("free -mh")
		os.system("clear")
	elif ch==6:
		exit()
			
