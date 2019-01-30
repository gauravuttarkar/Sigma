import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

options = ["Web", "Local" , "QnA"]

def on_button(option):
	print(option)
	if option == "Local":
		pass
		"""GAURAV FUNCTION"""
	elif option == "Web":
		query = searchBox.get()
		#query = searchBox.get().replace(" ", "+")
		#driver = webdriver.Chrome(executable_path = "/home/vrushank/Sigma/chromedriver")

		driver = webdriver.Firefox(executable_path = "/home/vrushank/Sigma/geckodriver")
		driver.get("http://www.google.com")
		a = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
		a.click()
		a.send_keys(query)
		driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()


		
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
photo= tk.PhotoImage(file="sigma1.png")
b.config(image=photo,width="30",height="30")
b.pack()


searchBox = tk.Entry(master, textvariable = "Type here to search! ",width = 60)
searchBox.pack()

for i,option in enumerate(options):
	B= tk.Button(master, text = option, command = lambda option=option:on_button(option))
	B.pack()



master.mainloop()
	