import random
import sqlite3
import useful_code as uc

class GameInfo:
	"""
	Class that stores all of the game's variables and has functions for events in the game that change them.
	"""
	def __init__(self):
		# sql
		connector = sqlite3.connect("other/choice_tree.db")
		self.sql = connector.cursor()

		# colours
		self.col = {
			"mia": "#ff0000",
			"p1": "#21a617",
			"p2": "#6e6e6e",
			"possessed p2": "#558057",
			"peter": "#007ade",
			"glitch peter": "#3c7ade",
			"jamie": "#ffff00",
			"gary": "#a00a0a",
			"ryan": "#0000b3",
			"matt": "#ff6e1f",
			"darren": "#ff6eff",
			"mikayla": "#8200ff",
			"white": "#ffffff",
			"black": "#000000",
			"red": "#ee0000",
			"blue": "#0000ff",
			"green": "#00ff00",
			"grey": "#bbbbbb"
		}

		# relationship levels
		self.rel = {
			"mia": 0,
			"p1": 0,
			"peter": 0,
			"jamie": 0,
			"gary": 0,
			"ryan": 0,
			"matt": 0,
			"darren": 0,
			"mikayla": 0
		}

		# names
		self.mia = "Narrator"
		self.p1 = "Player 1"
		self.p2 = "Player 2"

		# carry-over variables
		self.deal = "none"
		self.opped = False
		self.times_glitched = 0
		self.act = 1
		self.completed_endings = []

		# single-playthrough variables
		self.items = []
		self.recent_end = "none"
		self.gary_knows_name = False

	def na(self, tree):
		pass

	def fetch_db(self, sql_code: str, apostrophe=False):
		temp = str(self.sql.execute(sql_code).fetchone()).replace("(", "").replace(")", "").strip("'")[:-1]
		if not apostrophe:
			temp = temp.replace("'", "")
		if len(temp.split(", ")) <= 1:
			return temp
		return temp

	def generate(self, question):
		# generating branches
		if len(question.questions) == 0:
			for c in question.button_codes:
				question.addResponse(c, Question(c))

	def format(self, text: str, speech_marks=True):
		"""
		Formats the text correctly
		Bold: B{}
		Glitched: G{}
		"""
		new_text = text.replace("\\", "'").replace("''", "'")
		if not speech_marks:
			new_text = new_text.strip('"')
		return new_text

g = GameInfo()


class Question:
	def __init__(self, code="AAA0"):
		# setting variables
		code = code.replace(",", "")
		self.speaker = g.fetch_db(f"SELECT name FROM Choices WHERE code = '{code}'").replace(",", "") + ":"
		if self.speaker == ":":
			self.speaker = ""
		self.s_col = g.col[g.fetch_db(f"SELECT colour FROM Choices WHERE code = '{code}'").replace(",", "")]
		self.f = g.fetch_db(f"SELECT function FROM Choices WHERE code = '{code}'").replace(",", "")
		self.questions = {}

		# fetching button name
		if code == "AAA1":
			self.button_text = "NONE"
			self.button_colour = "#ffffff"
		else:
			bt1 = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE choice_codes LIKE '%{code}%'").split(", ")
			bt2 = g.fetch_db(f"SELECT button_codes FROM Choices WHERE choice_codes LIKE '%{code}%'").split(", ")
			try:
				bt3 = bt2[bt1.index(code + ",")][:-1]
			except:
				bt3 = bt2[bt1.index(code)]
			self.button_text = g.format(g.fetch_db(f"SELECT display_text FROM Buttons WHERE code = '{bt3}'", True))[:-1]
			self.button_colour = g.col[g.fetch_db(f"SELECT colour FROM Buttons WHERE code = '{bt3}'", True)[:-1]]
		self.button_codes = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE code = '{code}'").split(", ")

		# aligning text
		self.question = ""
		temp_q = g.format(g.fetch_db(f"SELECT speech FROM Choices WHERE code = '{code}'", True)[:-1], False)
		if len(temp_q) > 50:
			pointer = 0
			t = 0
			for i in range(len(temp_q)):
				try:
					if temp_q[i] == " " and temp_q[i + 1:].index(" ") + i - pointer > 50:
						self.question += "\n"
						if pointer == 0:
							t = i
						pointer = i - 1
					else:
						self.question += temp_q[i]
				except:
					if len(temp_q) - pointer > 50 and temp_q[i] == " ":
						self.question += "\n"
						if pointer == 0:
							t = i
						pointer = i - 1
					else:
						self.question += temp_q[i]
		else:
			self.question = temp_q

		if len(self.speaker) < len(self.question):
			if len(self.question) > 50:
				self.speaker += " " * (t - len(self.speaker))
			else:
				for i in range(0, len(self.question) - len(self.speaker)):
					self.speaker += " "

	def addResponse(self, code: str, q):
		self.questions[code] = q
		
	def addResponses(self, qs):
		for q in qs:
			self.questions[q[0]] = q[1]
			

# generating choice tree
qtree = Question("AAA1")