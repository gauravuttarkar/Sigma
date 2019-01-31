import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, uic

import tkinter as tk

options = ["Web", "Local" , "QnA"]

def on_button(option):
	print(option)
	if option == "Local":
		pass
		"""GAURAV FUNCTION"""
		
	elif option == "Web":
		query = searchBox.get().replace(" ", "+")
		app = QtWidgets.QApplication(sys.argv)
		path_ui = os.path.join(os.path.dirname(__file__), "test.ui")
		window = uic.loadUi(path_ui)
		window.widget.load(QtCore.QUrl("https://www.duckduckgo.com/?q="+ query ))
		window.show()
		sys.exit(app.exec_())


	elif option == "QnA":
		pass
		"""Shrinivas FUNCTION"""	


def on_search():
	print(searchBox.get())


def create():
	master = tk.Tk()
	master.title('Sigma Σ')
	master.geometry("%dx%d" % (1000, 500))

	b= tk.Button(master,command = on_search)
	photo= tk.PhotoImage(file="sigma1.png")
	b.config(image=photo,width="30",height="30")
	b.pack()


	searchBox = tk.Entry(master, textvariable = "Type here to search! ",width = 60)
	searchBox.pack()

	for i,option in enumerate(options):
		B= tk.Button(master, text = option, command = lambda option=option:on_button(option))
		B.pack()
	master.mainloop()

create()

	