import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, uic
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
options = ["Web", "Local" , "QnA"]

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
		for command in commandList:
			print(command)
			if len(command) > 0:
				os.system("gnome-open " + command)
		pass
		"""GAURAV FUNCTION"""
		
	elif option == "Web":
		query = searchBox.get().replace(" ", "+")
		app = QtWidgets.QApplication(sys.argv)
		path_ui = os.path.join(os.path.dirname(__file__), "test.ui")
		window = uic.loadUi(path_ui)
		window.widget.load(QtCore.QUrl("https://www.duckduckgo.com/?q="+ query ))
		window.show()
		app.exec_()
		window.destroy()
		app.destroy()


	elif option == "QnA":
		pass
		"""Shrinivas FUNCTION"""	


def on_search():
	print(searchBox.get())



master = tk.Tk()
master.title('Sigma Σ')
master.geometry("%dx%d" % (1000, 500))

b= tk.Button(master,command = on_search)
#img = Image.open("sigma1.png")
photo= tk.PhotoImage(file="sigma1.png")
b.config(width="30",height="30")
b.pack()


searchBox = tk.Entry(master, textvariable = "Type here to search! ",width = 60)
searchBox.pack()

for i,option in enumerate(options):
	B= tk.Button(master, text = option, command = lambda option=option:on_button(option))
	B.pack()
master.mainloop()


	