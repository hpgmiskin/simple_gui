#window.py
import tkinter,sys,time

class Window():
	"""Window class for Tkinter that creates a window that can have
	differnt GUI componeent added through differnt methods
	"""

	def __init__(self):
		self.root = tkinter.Tk()

	def setLevel(self,level=1):
		"method to set the level of the window"

		self.root.wm_attributes("-topmost", level)

	def setTitle(self,title):
		"method to set the title of the window"

		self.root.title(title)

	def addText(self,text):
		"method to add a text field to the window"

		if (type(text) == list):
			characterCount = max([len(line) for line in text])
			text = [line+" "*(characterCount-len(line)) for line in text]
		elif (type(text) == str):
			characterCount = len(text)
			text = [text]

		lineCount = len(text)
		tkText = tkinter.Text(self.root, width=characterCount, height=lineCount)

		for line in text:
			tkText.insert(tkinter.INSERT,line)

		tkText.pack()

	def addInput(self):
		"method to add a text input area to the window"

		self.entry = tkinter.Entry(self.root)
		self.entry.pack()

	def setInput(self):
		"method to set the class variable to that of the text input"

		self.input = self.entry.get()
		self.root.destroy()

	def getInput(self):
		"method to get the text input entry and close the current window"

		return self.input

	def addCanvas(self,height):
		"method to add a canvus to the current window"

		self.canvas = tkinter.Canvas(self.root, width = self.width, height = height, bg = "SteelBlue2")
		self.canvas.pack()

	def addButtons(self):
		"method to add a standard close button"

		self.button = tkinter.Button(self.root, text='End', command= lambda: self.quit())
		self.button.pack(side=tkinter.LEFT)

	def createStandard(self,title):
		"creates a standard window"

		self.setLevel()
		self.setTitle(title)

	def show(self):
		"shows the window in its current state"

		self.root.mainloop()

	def quit(self):
		"method to quit the current window and end the program"

		self.root.destroy()
		sys.exit()

class MessageBox(Window):
	"""MessageBox is a subclass of window and adds messgae box specific features though its methods"""
	def __init__(self):
		super().__init__()

	def setTitle(self,title):
		"set title of the message box with message box prefix"
		super().setTitle("Message Box - {}".format(title))

	def addButtons(self):
		"method to add message box specific buttons"

		button = tkinter.Button(self.root, text="Ok", command=self.root.destroy)
		button.pack(side=tkinter.LEFT)

		super().addButtons()

	def createStandard(self,title,text):
		"method to create a standard text box"

		super().createStandard(title)

		self.addText(text)
		self.addButtons()
		self.show()

class TextInput(Window):
	"""TextInput is a subclass of window and adds text input specfic features through its methods"""

	def __init__(self):
		super().__init__()

	def setTitle(self,title):
		super().setTitle("Text Input - {}".format(title))

	def addButtons(self):
		"method to add message box specific buttons"

		button = tkinter.Button(self.root, text="Submit", command=lambda: self.setInput())
		button.pack(side=tkinter.LEFT)

		super().addButtons()

	def createStandard(self,title):
		"method to create a standard text box"

		super().createStandard(title)
		
		self.addInput()
		self.addButtons()
		self.show()
		output = self.getInput()

		return output

def testLoop():
	"function to classtest message box infinitely"

	text = "blank"
	i=1
	while True:
		MessageBox().createStandard("title",["content 1 - this is the first line","content 2 - this is the second line",text])
		text = TextInput().createStandard("title")
		i += 1
		time.sleep(1)

testLoop()