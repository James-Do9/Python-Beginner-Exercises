import random

def get_randomInt():
	random_number = random.randrange(1,13)
	return random_number
"""How randrange works: the first parameter is where the number starts at and is included. The second 
parameter is where the number stops at and does not include the said number"""


print(get_randomInt())