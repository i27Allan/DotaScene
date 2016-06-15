# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
from datetime import datetime
##############################################

################GLOBAL VARIABLES################
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
accountDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\Accounts\\"
responseArray = []
################################################

def optionOne(api, myAccountID):
	print("What's the account ID?")
	targetAccountID = int(input())
	matchList = getMatchHistory(targetAccountID, api)
	getMatchDetails(matchList, targetAccountID, api)
	printResults()
	updateAccountOne(myAccountID, targetAccountID)

def getMatchHistory(targetAccountID, api):
	while (1):
		try:
			matchList = api.get_match_history(account_id=targetAccountID)
			print("We got the match history with success")
			break
		except:
			print("Error on getting match history")
	return (matchList)

def getMatchDetails(matchList, targetAccountID, api):
	matches = matchList['matches']
	index = matchList['num_results']
	for x in range(0, index):
		matchAux = organizeMatches(matches, x)
		while(1):
			try:
				getPlayerInfo(api.get_match_details(matchAux), targetAccountID)
				print("We got match number " + str(x + 1) + " with success")
				break
			except:
				print("Error on getting match number " + str(x + 1))

def organizeMatches(matches, index):
	match = matches[index]
	return (match['match_id'])

def getPlayerInfo(match, targetAccountID):
	players = match['players']
	x = 0
	while(1):
		player = players[x]
		if (player['account_id'] == targetAccountID):
			responseArray.append(player['account_id'])
			break
		x = x + 1

	responseArray.append(player['hero_name'])
	responseArray.append(player['kills'])
	responseArray.append(player['deaths'])
	responseArray.append(player['assists'])
	responseArray.append(player['last_hits'])
	responseArray.append(player['denies'])

def printResults():
	aux = 0
	for x in range(0, 100):
		with open(fileDirectory + str(responseArray[0]) + ".txt", "a") as toCreate:
			toCreate.write(str(responseArray[0]) + " as " + str(responseArray[aux+1]) + "\n")
			toCreate.write(str(responseArray[aux+2]) + "/" + str(responseArray[aux+3]) + "/" + str(responseArray[x+4]) + "\n")
			toCreate.write(str(responseArray[aux+5]) + "/" + str(responseArray[aux+6]) + "\n\n")
		aux = aux + 7

def updateAccountOne(myAccountID, targetAccountID):
	nowTime = datetime.now()
	with open(accountDirectory + str(myAccountID) + ".txt", "a") as saveConsult:
		saveConsult.write("("+str(nowTime.day) + "/" + str(nowTime.month) + "/" + str(nowTime.year) + " - " + str(nowTime.hour) + ":" + str(nowTime.minute) + ") - " + str(myAccountID) + " user has consulted " + str(targetAccountID) + " last played matches\n")