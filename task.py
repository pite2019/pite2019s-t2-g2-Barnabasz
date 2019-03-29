#!/usr/bin/env python3

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
