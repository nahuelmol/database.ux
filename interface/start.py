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
		self._add_country = tk.Button(self)
		self._add_country["text"] = "Add country"
		self._add_country["command"] = self.add_country
		self._add_country.pack(side="right")

		self._delete_country = tk.Button(self)
		self._delete_country["text"] = "Delete country"
		self._delete_country["command"] = self.delete_country
		self._delete_country.pack(side="right")

		self._update_country = tk.Button(self)
		self._update_country["text"] = "Update country"
		self._update_country["command"] = self.update_country
		self._update_country.pack(side="right")

	def add_country(self):
		print("\nTime to add some country")

	def delete_country(self):
		print("\nTime to delete a country")

	def update_country(self):
		print("\nTime to update a country")


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

