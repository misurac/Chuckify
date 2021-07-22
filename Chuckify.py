import requests

class ChuckFact:
	def __init__(self, value):
		self.value = value

	def info(self):
		print(self.value)

def getRandomChuckFact():
	response = requests.get("https://api.chucknorris.io/jokes/random")
	data = response.json()
	return data['value']

def convertToChuckFact(fact):
	myChuckFact = ChuckFact(fact)
	return myChuckFact.value

def openForWriting(fact):
	with open('myfacts.txt', 'a') as file:
		file.write(fact)
		file.write('\n')

def openForReading():
	with open('myfacts.txt', 'r') as file:
		lines = file.readlines()
		for line in lines:
			print(line)

def main():
	fact = getRandomChuckFact()
	openForWriting(fact)
	openForReading()

if __name__ == "__main__":
	main()





