#!/usr/bin/python

import random
while True:
	user_input=  int(raw_input("Press 1 for giving input right now!\nPress 2 for giving input by a file.\nPress 3 for exit.\nEnter::-"))
	if(user_input==1):
		user_listinput=raw_input("Enter Text you want to scramble::-")	
		words=user_listinput.split()
		scrambled_words=[]
		for i in words:
			if(len(i)<=3):
				scrambled_words.append(i)
				scrambled_words.append(" ")
			else:
				first_list=[]
				second_list=[]
				final_list=[]
				first_list.append(words[words.index(i)][0])			
 				second_list.append(words[words.index(i)][-1])
				for letter in i:
					final_list.append(letter)
				final_list.pop(0)
				final_list.pop(-1)
				x=[m for m in final_list]
				random.shuffle(x)
				x.insert(0,first_list)
				x.insert(len(x),second_list)
				output_list=[]
				for a in x:
					if(type(a).__name__=='str'):
						output_list.append(a)
					else:
						fullstr=''.join(a)
						output_list.append(fullstr)
				output_string="".join(output_list)
				scrambled_words.append(output_string)
				scrambled_words.append(" ")
				del first_list[:]
				del second_list[:]
				del final_list[:]
				del x[:]	
				del output_list[:]		
		print "Output="+''.join(scrambled_words)
	if(user_input==2):
		print "Under construction"
	if(user_input==3):
		exit();			
	
