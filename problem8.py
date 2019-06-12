#!/usr/bin/python3

import os
from gtts import gTTS
cmd=input("Enter something:-")
os.system("touch commands.txt")
statinf=os.path.getsize("commands.txt")
a=os.system(cmd +" 2>/dev/null")
if a==0:
	if statinf == 0:
		f=open("commands.txt","w+")
		f.write(cmd+" \n")
		f.close()
	else:
		f=open("commands.txt","a+")
		f.seek(0)
		lines=f.read().split("\n")
		command=cmd+" "
		if command in lines:
			tts = gTTS(text="Never run the same command", lang='en')			  
			tts.save("comd.mp3")
			os.system("xdg-open comd.mp3 ")
			
		else:
			pass
		f.write(cmd+" \n")
		f.close()
else:
	print("Wrong command!")
	f=open("commands.txt","a+")
	f.write(cmd+" \n")
	f.close()
