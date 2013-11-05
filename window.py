#window.py

class Window():
	"""Window class for Tkinter that creates a window that can have
	differnt GUI componeent added through differnt methods
	"""
	def __init__(self, width):
		self.width = width
		print("int")

	def setTitle(self,title):
		"method to set the title of the window"

		self.title = title
		print(self.width)
		print(title)

	def quit(self):
		"method to quit the current window and end the program"

class MessageBox(Window):
	"""MessageBox is a subclass of window and adds messgae box specific features though its methods"""
	def __init__(self, width):
		super().__init__(width)

	def setTitle(self,title):
		super().setTitle("Message Box - {}".format(title))


class TextInput(Window):
	"""TextInput is a subclass of window and adds text input specfic features through its methods"""

	def __init__(self,width):
		super().__init__(width)

	def setTitle(self,title):
		super().setTitle("Text Input - {}".format(title))

if True:
	messageBox = MessageBox(200)
	messageBox.setTitle("hello")