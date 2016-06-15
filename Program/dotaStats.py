# Owner: Vinícius Aguiar de Oliveira
# Program I'm coding to learn the dota2api and maybe use it afterwards as an opening to start on the e-sports scence, you never know.

##################IMPORTS#####################
import dota2api

import greetings
import o1
import o2
##############################################

################GLOBAL VARIABLES################
fileDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\txtResults\\"
accountDirectory = "C:\\Users\\Vinícius\\Documents\\UFPE\\Coding\\Python\\Dota\\Accounts\\"
################################################

def main():
	myAccountID = greetings.login()
	option = greetings.greetings()
	if (option == 0):
		return
	elif (option == 1):
		o1.optionOne(api, myAccountID)
	elif (option == 2):
		o2.optionTwo()

##########################RUNNER##########################
print("What is your API Key?")
apiKey = input()
api = dota2api.Initialise(apiKey)
main()
##########################################################
