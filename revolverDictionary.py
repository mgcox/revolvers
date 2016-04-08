import httplib
import json
from datetime import datetime


#Encodes Revolver
def encodeRevolver( str ):
	return str.encode("hex")

#This is just one type of revolver, there could be hundreds of revolvers that each individual user uses as their revolver
def getHourRevoler():
	currentTime = datetime.now()
	hour = currentTime.hour
	encodedVersion = str(hour).encode("hex")
	return encodedVersion

#This is just one type of revolver, there could be hundreds of revolvers that each individual user uses as their revolver
def getLocalMinuteRevoler():
	currentTime = datetime.now()
	minute = currentTime.minute
	encodedVersion = str(minute).encode("hex")
	return encodedVersion

def getManchesterScoreFromLastHomeGame():
	connection = httplib.HTTPConnection('api.football-data.org')
	headers = { 'X-Auth-Token': '3e98fe408a44493faaaec7668614b2cb', 'X-Response-Control': 'minified' }
	connection.request('GET', '/v1/teams/66/fixtures?timeFrame=p14&venue=home', None, headers )
	response = json.loads(connection.getresponse().read().decode())
	score = response["fixtures"][0]["result"]["goalsHomeTeam"]
	result = encodeRevolver(str(score))
	return result
