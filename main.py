import tkinter as tk
from tkinter.font import Font
import tkmacosx as tkm
import os
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
	def __init__(self, title: str, icon: str, main_win: bool):
		# set up the window
		if main_win:
			self._window = tk.Tk()
		else:
			self._window = tk.Toplevel()
		self._setup(title, icon)

	def _setup(self, title: str, icon: str):
		# colour scheme
		self._bg = "#000000"
		self._fg = "#ffffff"
		self._button_bg = Hex.apply_contrast(self._bg, self._fg, 0.2)
		self._button_fg = Hex.apply_contrast(self._fg, self._bg, 0.2)
		self._key = ""
		self._prev_key = ""

		# setup window
		self._window.title(title)
		self._window.wm_iconphoto(True, tk.PhotoImage(file=icon))
		self._window.config(bg=self._bg)
		self._window.bind("<Key>", self.key_handler)

		# fonts
		self._font = Font(
			family="Fixedsys Excelsior 3.01",
			size=32,
			weight="normal"
		)
		self._button_font = Font(
			family="Fixedsys Excelsior 3.01",
			size=20,
			weight="normal"
		)

		self.speaker = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=self._font)
		self.question = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=self._font)
		self._buttons = []
		self._spaces = []

	def key_handler(self, event):
		self._key = event.char
		self._prev_key = self._key

	def make_button(self, text, command, colour: str):
		return tkm.Button(self._window, text=text, command=command, bg=self._button_bg, activebackground=self._button_bg, fg=colour, font=self._button_font)

	def make_command(self, question):
		return lambda: self.show(question)

	def show(self, question):
		# clearing old screen
		if len(self._buttons) > 0:
			for button in self._buttons:
				button.destroy()
			for space in self._spaces:
				space.destroy()

		# creating new screen
		if len(question.questions) == 0:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10)).pack()
			self.make_button("Game Over", exit, "#ee0000").pack()
		else:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			for (q, a) in question.questions.items():
				space = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10))
				space.pack()
				self._spaces.append(space)
				button = self.make_button(a.button_text, self.make_command(a), a.button_colour)
				button.pack()
				self._buttons.append(button)
		self.q = question

	def start(self):
		self._window.focus_force()
		self._window.mainloop()


class Menu(Window):
	def __init__(self):
		self.__started = False
		Window.__init__(self, "TGG Menu", "assets/icon.png", True)
		self.speaker.pack()
		self.question.pack()

		# extra windows
		self.__game = Game(qtree)
		self.__game._window.destroy()
		self.__save_win = Window("TGG Save Menu", "assets/icon.png", False)
		self.__save_win._window.destroy()
		self.__load_win = Window("TGG Load Menu", "assets/icon.png", False)
		self.__load_win._window.destroy()

		self.show()

	def show(self):
		title_font = Font(
			family="Fixedsys Excelsior 3.01",
			size=64,
			weight="bold"
		)

		# list of buttons (name, colour, function)
		buttons = [
			["Start Game", "#00EEEE", "start"],
			["Save", "#00DD00", "save"],
			["Load", "#EE6600", "load"],
			["Open Choices Map", "#0088EE", "choices_map"],
			["Completed Endings", "#DD00EE", "endings_list"],
			["Quit", "#CC0000", "quit"]
		]

		# creating screen
		self.question.config(text="The Game of Glitches", fg="red", font=title_font)
		for b in buttons:
			space = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10))
			space.pack()
			self._spaces.append(space)
			button = self.make_button(b[0], getattr(self, "_" + b[2]), b[1])
			button.pack()
			self._buttons.append(button)

	def _start(self):
		try:
			self.__game._window.deiconify()
		except:
			self.__game = Game(qtree)

	def _save(self):
		try:
			self.__save_win._window.deiconify()
		except:
			self.__save_win = Window("TGG Save Menu", "assets/icon.png", False)
			tk.Label(self.__save_win._window, text="", bg=self._bg).pack()
			tk.Label(self.__save_win._window, text = "Type what you want to call your new save slot below and press the button to save.", font=self._font, bg=self._bg).pack()
			tk.Label(self.__save_win._window, text="", bg=self._bg).pack()
			self.__save_win.entry = tk.Entry(self.__save_win._window)
			self.__save_win.entry.pack()
			tk.Label(self.__save_win._window, text="", bg=self._bg).pack()
			self.__save_win.make_button("Save", self.__save_save_slot, "white").pack()
			tk.Label(self.__save_win._window, text="", bg=self._bg).pack()
			self.__save_win.message = tk.Label(self.__save_win._window, text="", bg=self._bg, font=self._button_font)
			self.__save_win.message.pack()

	def __save_save_slot(self):
		slot = self.__save_win.entry.get()
		if slot == "":
			self.__save_win.message.config(text="Save failed. Please do not use an empty name.", fg="#BB0000")
		elif slot == "default":
			self.__save_win.message.config(text="Save failed. Please do not save over the default slot.", fg="#BB0000")
		elif any(char in slot for char in " ,/()[]{}'"):
			self.__save_win.message.config(text="Save failed. Please do not include bad special characters or spaces.", fg="#BB0000")
		else:
			with open(f"save_slots/slot_{slot}.txt", "w") as file:
				file.write(self.__game.q.get_game_info())
			self.__save_win.message.config(text=f'File "slot_{slot}" saved succefully.', fg="#BB0000")
			self.__save_win.entry.delete(0, "end")

	def _load(self):
		try:
			self.__load_win._window.deiconify()
		except:
			self.__load_win = Window("TGG Load Menu", "assets/icon.png", False)
			tk.Label(self.__load_win._window, text="", bg=self._bg).pack()
			tk.Label(self.__load_win._window, text="Select what save slot from the drop down menu below you want to load.", font=self._font, bg=self._bg).pack()
			tk.Label(self.__load_win._window, text="", bg=self._bg).pack()

			slots = os.listdir("save_slots/")
			slots.sort()
			for i in range(len(slots)):
				slots[i] = slots[i][:-4]
			self.__load_win._selected = tk.StringVar()
			self.__load_win._selected.set("slot_default")
			self.__load_win._save_slots = tk.OptionMenu(self.__load_win._window, self.__load_win._selected, *slots)
			self.__load_win._save_slots.pack()
			tk.Label(self.__load_win._window, text="", bg=self._bg).pack()
			tkm.Button(self.__load_win._window, text="Load", command=self.__load_save_slot, fg=self._button_fg, bg=self._button_bg, font=self._button_font).pack()

	def __load_save_slot(self):
		selected = self.__load_win._selected.get()
		if os.path.exists(f"save_slots/" + selected):
			with open(f"save_slots/" + selected, "r") as file:
				try:
					self.__game._window.destroy()
				except:
					pass
				self.__game = Game(self.__game.q.set_game_info(file.read().split("\n")))

	def _choices_map(self):
		try:
			self.__map_win._window.deiconify()
		except:
			self.__map_win = Window("TGG Choices Map", "assets/icon.png", False)

			# making the flowchart
			canvas = tk.Canvas(self.__map_win._window, width=300, height=300, bg=self._bg, highlightthickness=0)
			canvas.pack(fill="both", expand=True)
			img = tk.PhotoImage(file="assets/placeholder.png")
			canvas.create_image(20, 20, anchor="nw", image=img)
			tk.mainloop()

	def _endings_list(self):
		try:
			self.__endings_win._window.deiconify()
		except:
			lesser_font = Font(
				family="Fixedsys Excelsior 3.01",
				size=24,
				weight="normal"
			)

			self.__endings_win = Window("TGG Endings List", "assets/icon.png", False)
			tk.Label(self.__endings_win._window, text="", bg=self._bg).pack()
			tk.Label(self.__endings_win._window, text="Endings", font=self._font, bg=self._bg).pack()
			scrollbar = tk.Scrollbar(self.__endings_win._window, highlightcolor="#FFFFFF")
			scrollbar.pack(side="right", fill="y")
			end_list = tk.Listbox(self.__endings_win._window, font=lesser_font, width=50, height=30, bg=self._bg, activestyle="none", exportselection=0)
			end_list.pack(fill="y")
			with open("memory/deaths_1.txt", "r") as file:
				info = file.read().split("\n")

			# formatting the endings list
			longest = len(max(info, key=len))
			for i in range(0, len(info), 2):
				end_list.insert("end", f"{info[i]}: {(longest + 1 - len(info[i])) * " "}{info[i + 1]}")
				if int(info[i + 1]) == 0:
					end_list.itemconfig(i // 2, foreground="#BB0000")
				else:
					end_list.itemconfig(i // 2, foreground="#009900")

			end_list.config(yscrollcommand=scrollbar.set)
			scrollbar.config(command=end_list.yview)

	def _quit(self):
		quit()


class Game(Window):
	def __init__(self, initialQ):
		Window.__init__(self, "The Game of Glitches", "assets/icon.png", False)
		self.speaker.pack()
		self.question.pack()

		# start the first question
		self.show(initialQ)

	def show(self, question):
		# running the function
		try:
			getattr(g, question.f)()
		except:
			pass
		if question.f == "quit":
			self._window.destroy()
		g.generate(question)

		# clearing old screen
		if len(self._buttons) > 0:
			for button in self._buttons:
				button.destroy()
			for space in self._spaces:
				space.destroy()

		# creating new screen
		if len(question.questions) == 0:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10)).pack()
			self.make_button("Game Over", exit, "#ee0000").pack()
		else:
			self.speaker.config(text=question.speaker, fg=question.s_col)
			self.question.config(text=question.question)
			for (q, a) in question.questions.items():
				space = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10))
				space.pack()
				self._spaces.append(space)
				button = self.make_button(a.button_text, self.make_command(a), a.button_colour)
				button.pack()
				self._buttons.append(button)
		self.q = question


Menu().start()