import tkinter as tk
from tkinter import ttk

# list_input, drop_down_input, (radio_input)
class UI: # listbox, combobox, radiobutton
	def __init__(self, window_title, default_com=None):
		self.__ui = tk.Tk()
		self.__ui.title(window_title)
		self.__dfcom = default_com
		self.__widget_list = []

	def title(self, label):
		self.__widget_list.append({
			"type": "title",
			"label": tk.Label(self.__ui, text=label)
		})

	def text_output(self, label, wid, df=""):
		if self.__name_available(wid):
			self.__widget_list.append({
				"id": wid,
				"type": "text_output",
				"label": tk.Label(self.__ui, text=label),
				"widget": tk.Label(self.__ui, name=wid)
			})
			self.__widget_list[-1]["widget"].configure(text=df)

	def number_output(self, label, wid, df=0, fmt="n"):
		if self.__name_available(wid):
			self.__widget_list.append({
				"id": wid, "format": fmt,
				"type": "number_output",
				"label": tk.Label(self.__ui, text=label),
				"widget": tk.Label(self.__ui, name=wid)
			})
			self.__widget_list[-1]["widget"].configure(text=df)

	def text_input(self, label, wid, df="", com=None):
		if self.__name_available(wid):
			if not com:
				com = self.__dfcom
			self.__widget_list.append({
				"id": wid,
				"type": "text_input",
				"label": tk.Label(self.__ui, text=label),
				"widget": tk.Entry(self.__ui, name=wid)
			})
			#self.__widget_list[-1]["widget"].set(df)
			self.__widget_list[-1]["widget"].delete(0, tk.END)
			self.__widget_list[-1]["widget"].insert(0, df)
			self.__widget_list[-1]["widget"].config(command=com)

	def number_input(self, label, wid, df=0, fr=None, t=None, i=None, fmt=float, com=None):
		if self.__name_available(wid):
			if not com:
				com = self.__dfcom
			self.__widget_list.append({
				"id": wid, "format": fmt,
				"type": "number_input",
				"label": tk.Label(self.__ui, text=label),
				"widget": ttk.Spinbox(self.__ui, name=wid, from_=fr, to=t, inc=i, width=9)
			})
			self.__widget_list[-1]["widget"].set(df)
			self.__widget_list[-1]["widget"].config(command=com)

	def boolean_input(self, label, wid, txt=None, df=False, com=None):
		if self.__name_available(wid):
			if not com:
				com = self.__dfcom
			var = tk.BooleanVar(value=df)
			self.__widget_list.append({
				"id": wid,
				"type": "boolean_input",
				"label": tk.Label(self.__ui, text=label),
				"variable": var,
				"widget": tk.Checkbutton(self.__ui, name=wid, text=txt, variable=var, onvalue=True, offvalue=False)
			})
			self.__widget_list[-1]["variable"].set(df)
			self.__widget_list[-1]["widget"].config(command=com)

	def slider_input(self, label, wid, df=0, fr=0, t=10, com=None):
		if self.__name_available(wid):
			if not com:
				com = self.__dfcom
			self.__widget_list.append({
				"id": wid,
				"type": "slider_input",
				"label": tk.Label(self.__ui, text=label),
				"widget": ttk.Scale(self.__ui, name=wid, from_=fr, to=t)
			})
			self.__widget_list[-1]["widget"].set(df)
			self.__widget_list[-1]["widget"].config(command=com)

	def button(self, label, wid=None, txt=None, com=None):
		if self.__name_available(wid):
			if not com:
				com = self.__dfcom
			self.__widget_list.append({
				"id": wid,
				"type": "button",
				"label": tk.Label(self.__ui, text=label),
				"widget": tk.Button(self.__ui, text=txt, name=wid, command=com)
			})

	def update(self):
		self.__ui.update()

	def mainloop(self):
		self.__ui.mainloop()

	def show(self):  # This makes the UI visible
		for i in range(len(self.__widget_list)):
			if self.__widget_list[i]["type"] == "title":
				self.__widget_list[i]["label"].grid(column=0, row=i, columnspan=2) # this is the title
			else:
				self.__widget_list[i]["label"].grid(column=0, row=i, sticky="E") # this is the label
				self.__widget_list[i]["widget"].grid(column=1, row=i, sticky="W") # this is the actual widget
		self.update()

	def get(self, arg):  # This returns the value of an input widget
		if self.__name_exists(arg):
			w = self.__get_widget_by_name(arg)
			if w["type"] == "number_input":
				return w["format"](w["widget"].get())
			elif w["type"] == "boolean_input":
				return w["variable"].get()
			else:
				return w["widget"].get()
		else:
			raise Exception("Widget name " + arg + " does not exist.")
			return None

	def set(self, arg, value):  # This sets the value of an input widget
		if self.__name_exists(arg):
			w = self.__get_widget_by_name(arg)
			if w["type"] == "number_input":
				w["widget"].set(str(value))
			elif w["type"] == "boolean_input":
				w["variable"].set(value)
			else:
				w["widget"].set(value)
		else:
			raise Exception("Widget name " + arg + " does not exist.")

	def output(self, arg, value):  # This sets the value of an output widget
		if self.__name_exists(arg):
			w = self.__get_widget_by_name(arg)
			if w["type"] == "number_output":
				w["widget"].configure(text=format(value, w["format"]))
			else:
				w["widget"].configure(text=value)
		else:
			raise Exception("Widget name " + arg + " does not exist.")

	def __get_widget_by_name(self, arg):  # return result
		for i in self.__widget_list:
			if i["type"] != "title" and i["id"] == arg:
				return i

	def __name_exists(self, arg):
		for i in self.__widget_list:
			if i["type"] != "title" and i["id"] == str(arg):
				return True
		return False

	def __name_available(self, arg):
		for i in self.__widget_list:
			if i["type"] != "title" and i["id"] == str(arg):
				raise Exception("Widget name " + arg + " already exists.")
				return False
		return True
