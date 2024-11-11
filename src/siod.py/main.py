import time
import siod

# Define the UI first
my_ui = siod.UI("Demo Window")

# Next define the callback functions for the widgets
def go():
	name = my_ui.get("name input")  # Text input returns a string
	year = my_ui.get("year input")  # Number input returns a number
	if name != "":  # Check if it's not the initial value
		# this is a text output so we should send it a string
		my_ui.output("greet output", "Greetings, " + name + "!")
	if year != 0:  # Check if it's not the initial value
		# this is a number output so we should send it a number
		my_ui.output("age output", int(time.strftime("%Y")) - year)

my_ui.title("----- Input section -----")
my_ui.text_input("Name", "name input")  # (label, ID)
my_ui.number_input("Year of birth", "year input", fmt=int)
my_ui.boolean_input("Bool", "bool input")
my_ui.slider_input("Slider", "slinput")
my_ui.title("----- Control section -----")
my_ui.button("Action", txt="GO!", com=go)
my_ui.title("----- Output section -----")
my_ui.text_output("Message:", "greet output")
my_ui.number_output("Age:", "age output")
my_ui.show()

while True:
	my_ui.update()
	time.sleep(0.01)
