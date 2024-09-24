import tkinter as tk
from tkinter.font import Font
import tkmacosx as tkm
from other.question_tree import qtree, g

class Hex:
	"""
	Class for hex/decimal conversion
	"""
	hexnumerals = "0123456789abcdef"

	@staticmethod
	def to_hex(number):
		hexString = ""
		while number > 0:
			hexString = Hex.hexnumerals[int(number % 16)] + hexString
			number //= 16
		return hexString

	@staticmethod
	def to_dec(hexString):
		offset = 1
		total = 0
		for i in hexString[::-1]:
			total += offset * Hex.hexnumerals.index(i)
			offset *= 16
		return total

	@staticmethod
	def split_colour(colour):
		return Hex.to_dec(colour[1:3]), Hex.to_dec(colour[3:5]), Hex.to_dec(colour[5:7])

	@staticmethod
	def apply_contrast(colour1, colour2, contrast):
		result = "#"
		c1 = Hex.split_colour(colour1)
		c2 = Hex.split_colour(colour2)
		for i in range(3):
			result += Hex.to_hex(c1[i] * 1 - contrast + c2[i] * contrast)
		return result


class Window:
	def __init__(self, initialQ):
		#Colour scheme
		self.__bg = "#000000"
		self.__fg = "#ffffff"
		self.__BUTTON_CONTRAST = 0.2
		self.__button_bg = Hex.apply_contrast(self.__bg, self.__fg, self.__BUTTON_CONTRAST)
		self.__button_fg = Hex.apply_contrast(self.__fg, self.__bg, self.__BUTTON_CONTRAST)

		# setup window
		self.__window = tk.Tk()
		self.__window.title("The Game of Glitches")
		self.__window.wm_iconphoto(True, tk.PhotoImage(file="other/icon.png"))
		self.__window.config(bg=self.__bg)

		# fonts
		self.__font = Font(
			family="Fixedsys Excelsior 3.01",
			size=32,
			weight="normal"
		)
		self.__button_font = Font(
			family="Fixedsys Excelsior 3.01",
			size=20,
			weight="normal"
		)

		self.speaker = tk.Label(self.__window, text="", bg=self.__bg, fg=self.__fg, font=self.__font)
		self.question = tk.Label(self.__window, text="", bg=self.__bg, fg=self.__fg, font=self.__font)
		self.speaker.pack()
		self.question.pack()
		self.__buttons = []
		self.__spaces = []

		# start the first question
		self.show(initialQ)

	def make_button(self, text, command, colour: str):
		return tkm.Button(self.__window, text=text, command=command, bg=self.__button_bg, activebackground=self.__button_bg, fg=colour, font=self.__button_font)

	def make_command(self, question):
		return lambda: self.show(question)

	def show(self, question):
		# running the function
		try:
			getattr(g, question.f)()
		except:
			pass
		if question.f == "quit":
			exit()
		g.generate(question)

		# clearing old screen
		if len(self.__buttons) > 0:
			for button in self.__buttons:
				button.destroy()
			for space in self.__spaces:
				space.destroy()

		# creating new screen
		if len(question.questions) == 0:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			tk.Label(self.__window, text="", bg=self.__bg, fg=self.__fg, font=("Consolas", 10)).pack()
			self.make_button("Game Over", exit, "#ee0000").pack()
		else:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			for (q, a) in question.questions.items():
				space = tk.Label(self.__window, text="", bg=self.__bg, fg=self.__fg, font=("Consolas", 10))
				space.pack()
				self.__spaces.append(space)
				button = self.make_button(a.button_text, self.make_command(a), a.button_colour)
				button.pack()
				self.__buttons.append(button)

	def start(self):
		self.__window.mainloop()

Window(qtree).start()