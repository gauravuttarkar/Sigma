import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
import platform
import os
import subprocess

API_KEY = "AIzaSyDKAjr9kU3Wb3aswdOc8fjCJT0xdOluB0c"

def IpAddress():
	pass


def calendar():
	command = "cal"
	ans = subprocess.check_output(command, shell=True);
	ans = str(ans,'utf-8').rstrip()
	print(ans)



def openFunction(tokens):
	print("Tokens",tokens)
	results = []
	commandList = []
	#if tokens[0] in ['file','document']:

	command = "sudo find /home -type f -name '" + tokens[0] + "'"  
	ans = subprocess.check_output(command, shell=True);
	command = str(ans,'utf-8').rstrip()
	commands = command.split("\n")
	for i in commands:
		commandList.append(i)
	print("in here")
	#os.system(command)
	#if tokens[0] in ['directory','folder']:
	command = "sudo find /home -type d -name '" + tokens[0] + "'"  
	#os.system(command)
	ans = subprocess.check_output(command, shell=True);
	#print(ans)
	command = str(ans,'utf-8').rstrip()
	commands = command.split("\n")
	for i in commands:
		commandList.append(i)
	#print(commands)
	for command in commandList:
		print(command)
		if len(command) > 0:
			os.system("gnome-open " + command)

def checkBrowser(tokens):

	synonyms = []

	        
	print(synonyms)

	google = []
	for syn in wordnet.synsets('website'):
	    for lemma in syn.lemmas():
	        google.append(lemma.name())
	print(google)

	for token in tokens:
		if token in ['google','Google'] :
			openBrowser() 




def checkFunctionality(tokens):
	print("Inside checkFunctionality")
	synonyms = []
	for syn in wordnet.synsets('start'):
	    for lemma in syn.lemmas():
	        synonyms.append(lemma.name())

	for syn in wordnet.synsets('open'):
	    for lemma in syn.lemmas():
	        synonyms.append(lemma.name())
	print(synonyms)
	for token in tokens:
		print("token")
		if token in synonyms:
			print("Inside openFunction")
			openFunction(tokens[1:]) 
	
	pass



def openBrowser():

	if platform.platform()[:5] == 'Linux':
		os.system("x-www-browser http://www.google.com")
	else:
		os.system('open "http://www.google.com"')


query = input("Enter your query\n")
#query = "asdfasdf"
tokens = word_tokenize(query)
print(tokens)


#Cleaning tokens from stopwords
clean_tokens = tokens[:] 
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)





print(clean_tokens)

checkFunctionality(tokens)

#IPaddress()
#openBrowser(["asd"])