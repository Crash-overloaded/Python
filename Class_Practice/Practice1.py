#!/usr/bin/python3

class Car():
	def __init__(self,modelname,yearofm,price):
		self.modelname = modelname
		self.yearofm = yearofm
		self.price = price

honda = Car('City',2017,1000000)
tata = Car('Nano',2016,200000)




print(honda.price)
