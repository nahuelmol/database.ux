import tkinter as tk
import time
import os

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.my_widgets()

	def my_widgets(self):
		self.functionalities = tk.Button(self)
		self.functionalities["text"]= "More options"
		self.functionalities["command"]=self.deploy_more_buttons
		self.functionalities.pack(side="top")
		self.quit = tk.Button(self, text="QUIT", fg="red",
		                      command=self.master.destroy)
		self.quit.pack(side="bottom")

	def deploy_more_buttons(self):
		print("\nDeploying new buttons and its functions")

	def add_country(self):
		print("\nTime to add some country")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")

    app = Application(master=root)
    app.mainloop()

if __name__ == "interface.start":
	root = tk.Tk()
	root.geometry("800x400")
	app = Application(master=root)
	app.mainloop()

print(__name__)