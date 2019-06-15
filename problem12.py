#!/usr/bin/python3

import pyqrcode
from googlesearch import search

data=input("Enter a query:-")
a=0
for i in search(data,tld="co.in",stop=3):
	a=a+1
	url=pyqrcode.create(i)
	url.svg("qrscan.svg"+str(a),scale=8)
