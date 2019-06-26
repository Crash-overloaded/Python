#!/usr/bin/python3
import os
cmd=input("Can you please enter command again:-")
with open(os.path.expanduser("~/.bashrc"),"r") as bash:
	d=bash.readlines()
	for i in d:
		if "alias "+cmd in i:
			print("ok")
		else:
			print("waapis bna")
