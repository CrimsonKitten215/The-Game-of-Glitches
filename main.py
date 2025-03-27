import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
import tkmacosx as tkm
from PIL import Image, ImageTk
import os
from useful_code.question_tree import qtree, g
import useful_code.type_convertor as tc


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

	def make_button(self, text, command, colour: str):
		return tkm.Button(self._window, text=text, command=command, bg=self._button_bg, activebackground=self._button_bg, fg=colour, font=self._button_font)

	# unused for now
	def key_handler(self, event):
		self._key = event.char
		self._prev_key = self._key

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
			self.__save_win.message.config(text=f'File "slot_{slot}" saved succefully.', fg="#00BB00")
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
		selected = self.__load_win._selected.get() + ".txt"
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

			# act checking
			act = g.get_act()
			if act == 0 or act == 4:
				# failsafe if in-between acts
				frame = tk.Frame(self.__map_win._window, width=300, height=300)
				frame.pack(expand=True, fill="both")
				canvas = tk.Canvas(frame, width=300, height=300, bg=self._bg, highlightthickness=0)
				canvas.pack(fill="both", expand=True)
				canvas.create_image(20, 20, anchor="nw", image=ImageTk.PhotoImage(Image.open("assets/map_unavailable.png")))
			else:
				# making the images
				images = []
				image = Image.open(f"assets/choices_map{act}/choices_map.png")
				images.append(ImageTk.PhotoImage(image))

				with open(f"memory/endings_{act}.txt", "r") as file:
					info = file.read().split("\n")
				for i in range(0, len(info), 2):
					if info[i + 1] != "0":
						image = Image.open(f"assets/choices_map{act}/{info[i].lower().replace(" ", "_")}.png")
						images.append(ImageTk.PhotoImage(image))

				# making the canvas
				frame = tk.Frame(self.__map_win._window, width=300, height=300)
				frame.pack(expand=True, fill="both")
				scrollbar_x = ttk.Scrollbar(frame, orient="horizontal")
				scrollbar_x.pack(side="bottom", fill="x")
				scrollbar_y = ttk.Scrollbar(frame)
				scrollbar_y.pack(side="right", fill="y")
				canvas = tk.Canvas(frame, width=300, height=300, bg=self._bg, highlightthickness=0, scrollregion=(0, 0, images[0].width() + 20, images[0].height() + 20))
				canvas.pack(fill="both", expand=True)
				canvas.config(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
				scrollbar_x.config(command=canvas.xview)
				scrollbar_y.config(command=canvas.yview)

				for i in images:
					canvas.create_image(20, 20, anchor="nw", image=i)
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
			scrollbar = ttk.Scrollbar(self.__endings_win._window)
			scrollbar.pack(side="right", fill="y")
			end_list = tk.Listbox(self.__endings_win._window, font=lesser_font, width=50, height=30, bg=self._bg, activestyle="none", exportselection=0)
			end_list.pack(fill="y")
			with open(f"memory/endings_{g.get_act()}.txt", "r") as file:
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
		self.q = question

		# running the function
		try:
			getattr(g, self.q.f)()
		except:
			pass
		if self.q.f == "quit":
			self._window.destroy()
		g.generate(self.q)

		# clearing old screen
		if len(self._buttons) > 0:
			for button in self._buttons:
				button.destroy()
			for space in self._spaces:
				space.destroy()

		# creating new screen
		if len(self.q.questions) == 0:
			self.speaker.config(text=self.q.speaker, fg=self.q.s_col)
			self.question.config(text=self.q.question)
			tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=("Consolas", 10)).pack()
			self.make_button("Game Over", exit, "#EE0000").pack()
		else:
			self.speaker.config(text=self.q.speaker, fg=self.q.s_col)
			self.question.config(text=self.q.question)
			if self.q.code == "AAB0" or self.q.code == "AAE0":
				self._add_space()
				self.entry = tk.Entry(self._window)
				self.entry.pack()
				self._add_space()
				button = self.make_button("Continue", self.__make_general_command(self.get_entry, self.q.questions[list(self.q.questions)[0]]), "grey")
				button.pack()
				self._buttons.append(button)
				self._add_space()
				self.message = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=self._button_font)
				self.message.pack()
			else:
				for (q, a) in self.q.questions.items():
					self._add_space()
					if self.q.code == "AAC0":
						button = self.make_button(a.button_text, self.__make_general_command(self.__set_gender, a), a.button_colour)
					elif self.q.code == "AAD0":
						button = self.make_button("Continue", self.make_command(a), g.col["grey"])
					else:
						button = self.make_button(a.button_text, self.make_command(a), a.button_colour)
					button.pack()
					self._buttons.append(button)

		if self.q.speaker[0] == ":":
			self.speaker.config(text="")

	def _add_space(self):
		space = tk.Label(self._window, text="", bg=self._bg, fg=self._fg, font=self._button_font)
		space.pack()
		self._spaces.append(space)

	def __set_gender(self, question):
		player = (g.get_act() // 4) + 1
		if question.button_text == "She/her":
			temp = "f"
		elif question.button_text == "He/him":
			temp = "m"
		else:
			temp = "n"

		g.transgenderfy(temp, player)
		self.set_info("memory/player_info.txt", 3, temp)
		g.set_act(player)
		self.set_info("memory/carry_over_info.txt", 1, player)
		self.show(question)

	def make_command(self, question):
		return lambda: self.show(question)

	def __make_general_command(self, command, input):
		return lambda: command(input)

	def get_entry(self, question):
		info = self.entry.get()
		if info == "":
			self.message.config(text="Please do not use an empty name.", fg="#BB0000")
		elif any(char.upper() == char.lower() and not char in " '\"1234567890" for char in info):
			self.message.config(text="Please do not include special characters.", fg="#BB0000")
		else:
			if g.get_act() <= 1:
				g.set_p1_name(info)
				self.set_info("memory/player_info.txt", 1, info)
			else:
				g.set_p2_name(info)
				self.set_info("memory/player_info.txt", 5, info)
			self.entry.destroy()
			self.message.destroy()
			self.show(question)

	@staticmethod
	def set_info(file_name: str, line: int, info: str):
		with open(file_name, "r") as file:
			text = file.read().split("\n")
		text[line] = info
		with open(file_name, "w") as file:
			file.write(tc.unlistify(text).replace(", ", "\n"))


Menu().start()