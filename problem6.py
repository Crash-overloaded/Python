#!/usr/bin/python3

import os
import subprocess as sp
cmd=input("Enter name of command you want to give:-")
loc=sp.getoutput("echo $(pwd)")
with open(os.path.expanduser("~/.bashrc"),"at") as bash:
	bash.write(
		"\n"
		'alias '+cmd+'="python3 "'+loc+'"/problem6_2file.py"\n'
	)
os.system("source ~/.bashrc")
os.system("python3 "+loc+"/problem6_2file.py")

