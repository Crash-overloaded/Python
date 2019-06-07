#!/usr/bin/python3

from gsearch.googlesearch import search
import time

data=input("Enter something you want to search:-")
results=search(data)
# checking if the list is empty or not
if not results:
	print("There was an technical error")
	time.sleep(2)
	print("Retrying....This may take upto 10-15 seconds")
# Retrying after 10-20 sec will not get exceed limit
	time.sleep(10)
	results=search(data)
	print(results)
else:
	print(results)
