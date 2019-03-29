#!/usr/bin/env python3

#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


class Bank:
	def __init__(self, name):
		self.name = name
		self.clients = {}
	def get_name(self):
		return self.name
	def add_client(self, name, maney = 0):
		self.clients[name] = Client(self.get_name(), maney)
	def get_client(self, name):
		return self.clients[name]
	def input(self, client, value = 0):
		self.clients[client].input(value)
	def withdrawal(self, client, value = 0):
		self.clients[client].withdrawal(value)
	def transfer(self, clientA, clientB, value):
		self.clients[clientA].transfer(self.clients[clientB], value)

class Client:
	def __init__(self, bankName, maney = 0):
		self.maney = maney
		self.bankName = bankName
	def get_maney(self):
		return self.maney
	def input(self, value):
		self.maney += value
	def withdrawal(self, value):
		self.maney -= value
	def transfer(self, clientB, value):
		self.maney -= value
		clientB.maney += value


bank1 = Bank("PEKAO")
bank1.add_client("Bogdan", 500)
bank1.add_client("Barnaba", 1000)



print(bank1.get_client("Bogdan").get_maney())
print(bank1.get_client("Barnaba").get_maney())
bank1.input("Barnaba", 200)
print(bank1.get_client("Barnaba").get_maney())
bank1.withdrawal("Bogdan", 200)
print(bank1.get_client("Bogdan").get_maney())
bank1.transfer("Barnaba","Bogdan", 1000)
print(bank1.get_client("Bogdan").get_maney())
print(bank1.get_client("Barnaba").get_maney())