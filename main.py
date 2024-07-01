import tkinter as tk
from tkinter.font import Font
from question_tree import qtree, g

class Hex:
	"""
	Class for hex/decimal conversion
	"""
	hexnumerals = [str(i) for i in range(10)] + "a,b,c,d,e,f".split(",")
	@staticmethod
	def toHex(number):
		hexString = ""
		while number > 0:
			hexString = Hex.hexnumerals[int(number % 16)] + hexString
			number //= 16
		return hexString

	@staticmethod
	def toDec(hexString):
		offset = 1
		total = 0
		for i in hexString[::-1]:
			total += offset * Hex.hexnumerals.index(i)
			offset *= 16
		return total

	@staticmethod
	def splitColour(colour):
		return (Hex.toDec(colour[1:3]), Hex.toDec(colour[3:5]), Hex.toDec(colour[5:7]))

	@staticmethod
	def applyContrast(colour1, colour2, contrast):
		result = "#"
		c1 = Hex.splitColour(colour1)
		c2 = Hex.splitColour(colour2)
		for i in range(3):
			result += Hex.toHex(c1[i] * 1-contrast + c2[i] * contrast)
		return result


class Window:
	def __init__(self, initialQ):
		#Colour scheme
		self.bg = "#000000"
		self.fg = "#ffffff"
		self.buttonContrast = 0.2
		self.buttonBG = Hex.applyContrast(self.bg,self.fg,self.buttonContrast)
		self.buttonFG = Hex.applyContrast(self.fg,self.bg,self.buttonContrast)

		# setup window
		self.window = tk.Tk()
		self.window.title("The Game of Glitches")
		self.window.config(bg=self.bg)

		# fonts
		self.font = Font(
			family="Fixedsys",
			size=32,
			weight="normal"
		)
		self.button_font = Font(
			family="Fixedsys",
			size=20,
			weight="normal"
		)
		self.name_font = Font(
			family="Fixedsys",
			size=25,
			weight="bold"
		)

		self.speaker = tk.Label(self.window, text="", bg=self.bg, fg=self.fg, font=self.name_font)
		self.question = tk.Label(self.window, text="", bg=self.bg, fg=self.fg, font=self.font)
		self.speaker.pack()
		self.question.pack()
		self.buttons = []
		self.spaces = []

		# start the first question
		self.show(initialQ)

	def makeButton(self, text, command, colour: str):
		return tk.Button(self.window, text=text, command=command, bg=self.buttonBG, fg=colour, font=self.button_font)

	def makeCommand(self, question):
		return lambda: self.show(question)

	def show(self, question):
		# running the function
		if question.f == "quit":
			exit()
		try:
			temp = getattr(g, question.f)(question)
		except:
			temp = None
		if temp != None:
			question = temp
		g.generate(question)

		# clearing old screen
		if len(self.buttons) > 0:
			for button in self.buttons:
				button.destroy()
			for space in self.spaces:
				space.destroy()

		# creating new screen
		if len(question.questions) == 0:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			tk.Label(self.window, text="", bg=self.bg, fg=self.fg, font=("Consolas", 10)).pack()
			self.makeButton("Game Over", exit, "#ee0000").pack()
		else:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			for (q, a) in question.questions.items():
				space = tk.Label(self.window, text="", bg=self.bg, fg=self.fg, font=("Consolas", 10))
				space.pack()
				self.spaces.append(space)
				button = self.makeButton(a.button_text, self.makeCommand(a), a.button_colour)
				button.pack()
				self.buttons.append(button)

	def start(self):
		self.window.mainloop()

Window(qtree).start()