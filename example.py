
# File: test.py

import hashlib
from datetime import datetime
from random import randrange
import difflib

#Encodes Revolver
def encodeRevolver( str ):
	return str.encode("hex")

#This is just one type of revolver, there could be hundreds of revolvers that each individual user uses as their revolver
def getHourRevoler():
	currentTime = datetime.now()
	hour = currentTime.hour
	encodedVersion = str(hour).encode("hex")
	print encodedVersion
	return encodedVersion

#This will return true or false depending on whether the password and revolver match or not
def checkValues(inputPassword, storedPassword):

	dif = difflib.SequenceMatcher(None, inputPassword, storedPassword)
	matchCount = 0
	difArray = dif.get_matching_blocks()

	removedHexString = ""
	revolver = inputPassword

	removedCount = 0

	for block in difArray[:-2]:
		removedHexString += inputPassword[block[0]:-(len(inputPassword)- (block[0]+block[2]))]
		revolver = revolver[:(block[0] - removedCount)] + revolver[((block[0]-removedCount)+block[2]):]
		removedCount += block[2]
	else:
		removedHexString += inputPassword[difArray[len(difArray) -2][0]:]
		revolver = revolver[:-difArray[len(difArray) -2][2]] 
	
	#64 characters will have matched the stored hash in the db and the revolver will match the users chosen revolver, in this case the hour revolver
	if len(removedHexString) == 64 and revolver == getHourRevoler():
		return True

	return False

def verify(passwordWithRevolver):
	#answer represents a hashed value stored in the DB, this is 68 chars long instead of 64 because it contains the revolver used the first time
	answer = "0b14d501a594442a01c68595413130bcb3e8164d183d32937b851835442f69d5c94e"
	attempt = checkValues(passwordWithRevolver, answer)
	return attempt



#The answer password is password1
#The revolver is the current hour 

password = raw_input("Please enter your password: ")
revolver = raw_input("Please enter your revolver: ")

#This example uses 
h = hashlib.sha256()
h.update(password.encode('utf-8'))
hashedPassword = h.hexdigest()
# get a random location to insert revolver into hashed password 
location = randrange(len(hashedPassword))

#encode the revolver entered by user
encodedRevolver = str(revolver).encode("hex")

#add revolver to random place in hashed string, this could be much more complex than just appending at random place
passwordWithRevolver = hashedPassword[:location] + encodedRevolver + hashedPassword[location:]


result = verify(passwordWithRevolver)

print result 








