import tkinter as tk
import webbrowser
import subprocess
import os
import azure.cognitiveservices.speech as speechsdk

options = ["Web", "Local" , "QnA"]
speech_key, service_region = "ce65e998f2fc4c64b8b4ef77d62d0518", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

def on_local(cmd):
	os.system("gnome-open " + cmd)

def voice():
	speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
	searchBox.delete(0,len(searchBox.get()))
	searchBox.insert(0,"Say something..")	
	result = speech_recognizer.recognize_once()
	if result.reason == speechsdk.ResultReason.RecognizedSpeech:
		print("Recognized: {}".format(result.text))
		searchBox.delete(0,len(searchBox.get()))
		searchBox.insert(0,result.text)
		return
	elif result.reason == speechsdk.ResultReason.NoMatch:
	    print("No speech could be recognized: {}".format(result.no_match_details))
	elif result.reason == speechsdk.ResultReason.Canceled:
	    cancellation_details = result.cancellation_details
	    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
	    if cancellation_details.reason == speechsdk.CancellationReason.Error:
	        print("Error details: {}".format(cancellation_details.error_details))
	pass
	return



def on_button(option):
	print(option)
	if option == "Local":
		query = searchBox.get()
		commandList = []
	#if tokens[0] in ['file','document']:

		command = "sudo find /home -type f -name '" + query + "'"  
		ans = subprocess.check_output(command, shell=True);
		command = str(ans,'utf-8').rstrip()
		commands = command.split("\n")
		for i in commands:
			commandList.append(i)
		print("in here")
		#os.system(command)
		#if tokens[0] in ['directory','folder']:
		command = "sudo find /home -type d -name '" + query + "'"  
		#os.system(command)
		ans = subprocess.check_output(command, shell=True);
		#print(ans)
		command = str(ans,'utf-8').rstrip()
		commands = command.split("\n")
		for i in commands:
			commandList.append(i)
		#print(commands)
		# for command in commandList:
		# 	print(command)
		# 	if len(command) > 0:
		# 		os.system("gnome-open " + command)
		# pass
		w = tk.Label(master, text="Results")
		w.pack()
		for i,cmd in enumerate(commandList):
			button = tk.Button(master, text = cmd,  command = lambda cmd=cmd:on_local(cmd)  )
			button.pack()

		"""GAURAV FUNCTION"""
	elif option == "Web":
		query = searchBox.get().replace(" ", "+")
		webbrowser.open('http://google.com/search?q='+query)

		"""My FUNCTION"""
	elif option == "QnA":
		pass
		"""Shrinivas FUNCTION"""	


def on_search():
	print(searchBox.get())



master = tk.Tk()
master.title('Sigma Σ')
master.geometry("%dx%d" % (1000, 500))

b= tk.Button(master,command = on_search)
voice = tk.Button(master,command = voice)
pic= tk.PhotoImage(file="finalMic.png")
voice.config(image=pic,width="30",height="30")

photo= tk.PhotoImage(file="sigma1.png")
b.config(image=photo,width="30",height="30")
b.pack()
voice.pack()


searchBox = tk.Entry(master, textvariable = "Type here to search! ",width = 60)
searchBox.pack()

for i,option in enumerate(options):
	B= tk.Button(master, text = option, command = lambda option=option:on_button(option))
	B.pack()



master.mainloop()
	