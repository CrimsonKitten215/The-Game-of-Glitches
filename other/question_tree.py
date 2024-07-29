import random
import sqlite3
import useful_code as uc

class GameInfo:
	"""
	Class that stores all of the game's variables and the functions for events in the game that change them.
	"""
	def __init__(self):
		# sql
		connector = sqlite3.connect("sql/choice_tree.db")
		self.__sql = connector.cursor()

		# colours
		self.col = {
			"mia": "#ff0000",
			"p1": "#21a617",
			"p2": "#6e6e6e",
			"possessed p2": "#558057",
			"peter": "#007ade",
			"glitched peter": "#3c7ade",
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
			"grey": "#bbbbbb",
			"gold": "#DB901C"
		}

		# relationship levels
		self.__rel = {
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

		# carry-over variables
		with open("memory/carry_over_info.txt", "r") as file:
			info = file.read().split("\n")
		self.act = int(info[1])
		if self.act != 1:
			self.__deal = info[3]
			self.__opped = info[5]
			self.__times_glitched = info[7]

			# change later when I figure out what each stage will be called
			if self.__deal == "possessed":
				self.__possessed = True

		# player info
		with open("memory/player_info.txt", "r") as file:
			info = file.read().split("\n")
		self.__p1_name = info[1]
		self.__p2_name = info[5]
		self.__transgenderfy(info[3], 1)
		self.__transgenderfy(info[7], 2)

		# single-playthrough variables
		self.__next_bfly_effect = 0
		self.__items = []
		self.__recent_end = "none"
		self.__gary_knows_name = False

	# basic functions
	def na(self):
		pass

	def __transgenderfy(self, gender: str, player: int):
		# changes the player's pronouns
		if gender == "f":
			temp = {
				"they": "she",
				"them": "her",
				"they're": "she's",
				"their": "her",
				"theirs": "hers",
				"themself": "herself",
				"person": "girl",
				"They": "She",
				"Them": "Her",
				"They're": "She's",
				"Their": "Her",
				"Theirs": "Hers",
				"Themself": "Herself",
				"Person": "Girl",
				"THEY": "SHE",
				"THEM": "HER",
				"THEY'RE": "SHE'S",
				"THEIR": "HER",
				"THEIRS": "HERS",
				"THEMSELF": "HERSELF",
				"PERSON": "GIRL"
			}
		elif gender == "m":
			temp = {
				"they": "he",
				"them": "him",
				"they're": "he's",
				"their": "his",
				"theirs": "his",
				"themself": "himself",
				"person": "guy",
				"They": "He",
				"Them": "Him",
				"They're": "He's",
				"Their": "His",
				"Theirs": "His",
				"Themself": "Himself",
				"Person": "Guy",
				"THEY": "HE",
				"THEM": "HIM",
				"THEY'RE": "HE'S",
				"THEIR": "HIS",
				"THEIRS": "HIS",
				"THEMSELF": "HIMSELF",
				"PERSON": "GUY"
			}
		else:
			temp = {
				"they": "they",
				"them": "them",
				"they're": "they're",
				"their": "their",
				"theirs": "theirs",
				"themself": "themself",
				"person": "person",
				"They": "They",
				"Them": "Them",
				"They're": "They're",
				"Their": "Their",
				"Theirs": "Theirs",
				"Themself": "Themself",
				"Person": "Person",
				"THEY": "THEY",
				"THEM": "THEM",
				"THEY'RE": "THEY'RE",
				"THEIR": "THEIR",
				"THEIRS": "THEIRS",
				"THEMSELF": "THEMSELF",
				"PERSON": "PERSON"
			}

		if player == 1:
			self.__p1_pronouns = temp
		else:
			self.__p2_pronouns = temp

	def fetch_db(self, sql_code: str, apostrophe=False):
		temp = str(self.__sql.execute(sql_code).fetchone()).replace("(", "").replace(")", "").strip("'")[:-1]
		if not apostrophe:
			temp = temp.replace("'", "")
		return temp

	def generate(self, question):
		# generating branches
		if len(question.questions) == 0:
			if len(question.button_codes) < len(question.choice_codes):
				question.choice_codes = [question.choice_codes[self.__next_bfly_effect]]
			for c in question.choice_codes:
				question.addResponse(c, Question(c))

	def __word_replacer(self, old_word: str, new_word: str, text: str):
		while old_word in text:
			temp = text.index(old_word)
			if temp == 0:
				text = new_word + text[len(old_word) + 4:]
			else:
				text = text[:temp] + new_word + text[temp + len(old_word):]
		return text

	def __formatter(self, text: str, char: str, new_alpha: list):
		alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
		new_text = text
		while char + "{" in new_text:
			start = 0
			end = -1
			for i in range(0, len(new_text) - 1):
				if new_text[i: i + 2] == char + "{":
					start = i
					i += 2
				if new_text[i] == "}":
					end = i
					break
			temp = ""

			# make more efficient somehow eventually
			for c in new_text[start + 2: end]:
				if c in alphabet:
					loc = alphabet.index(c)
					temp += new_alpha[loc][random.randint(0, len(new_alpha[loc]) - 1)]
				else:
					temp += c

			new_text = self.__word_replacer(new_text[start: end], temp, new_text).replace("}", "")
		return new_text

	def format(self, text: str, speech_marks=True):
		"""
		Formats the text correctly.

		Formatting codes/keys:
		Glitched: G{}
		Variables: V{}
		P1 Pronouns: P1{}
		P2 Pronouns: P2{}
		(): []
		"""

		# alphabets
		glitched_letters = [
			list("AĀĂĄȀȂȦÀÁÃÄÅǍǞǠǺȺӐӒΆἈἉἊἋἌἍἎἏᾈᾉᾊᾋᾌᾍᾎᾏᾸᾹᾺΆᾼ"),
			list("BƁƂɃᛒḂḄꞖḆꞴ"),
			list("CĆĈƇʗℂÇĊČḈℭꞒꜾ"),
			list("DĐƉⅅĎƊḊḌḎḐḒ"),
			list("EĒĔĖĘȄȆȨɆÈÉÊËĚƎ"),
			list("FƑℲḞꞘꟻ"),
			list("GĠĢƓ⅁ĜĞǤǦǴḠ𝔾𝕲"),
			list("HĤĦȞᚻᚺḢḤḦḨḪℌℍⱧꞪＨ𝓗"),
			list("IĨİƗȈÌÍÎÏĪĬĮǏȊ"),
			list("JĴ𝔍𝕁𝒥"),
			list("KĶƘKǨḰḲḴⱩꝀꝂꝄꞢꞰ𝒦𝓚𝕂"),
			list("LĹŁĽĻĿḶḸḺḼⱠⱢꝆꝈꞭ"),
			list("MℳḾṀṂⱮꟽ𝓜𝔐𝕄"),
			list("NŃŅŇȠℕÑƝǸṄṆṈṊ∏⋂ꞤꞐ"),
			list("OŐȰÒÓÔÕÖØŌŎƟƠǑǪǬǾȌȎȪȬȮӦӨӪ"),
			list("PℙƤṔṖⱣꝐꝒꝔꟼ𝓟"),
			list("QɊℚ℺ꝘꝖ𝒬"),
			list("RŔŖŘȐȒɌᚱṘṚṜⱤℝℜṞꝚꞦꭆ"),
			list("SŠȘŚŜŞṤṢṠṦṨⱾꞨ"),
			list("TŢŤŦƬƮȚȾᛏṪṬṮṰ𝒯𝕋"),
			list("UŨŰȔŲɄȖÙÚÛÜŪŬŮƯǓǕǗǙǛ"),
			list("VṼṾ𝒱𝕍"),
			list("WŴẀẂẄẆẈⱲ𝒲𝕎"),
			list("X✘ẊẌ𝒳𝔛𝕏"),
			list("YŶŸȲÝ⅄ƳɎẎỲỴỶỸ𝕐"),
			list("ZŹȤℤŻŽƵẐẒẔⱿⱫ𝒵"),
			list("aāăąȁȃȧɐàáâãäåǎǟǡǻӑӓ"),
			list("bƀƃɓᵬᶀḃḅḇ"),
			list("cćĉƈɕↄçċčȼḉꜿꞓꞔ"),
			list("dđȡɖɗƌďᶑᶁᵭḋḍḏḑḓ"),
			list("eēĕėęȅȇȩɇɘèéêëěǝ"),
			list("fƒᵮᶂḟꞙ"),
			list("gġģɠĝğǥǧǵᶃᵷḡꞡꬶ"),
			list("hĥħɦȟḣḥḧḩḫẖⱨꞕ𝕙"),
			list("iĩıȉɨìíîïīĭįǐȋ"),
			list("jĵȷɉĵǰɟʝ𝕛"),
			list("kķƙǩʞḱᶄḳⱪḵꝁꝃꝅꞣ𝕜"),
			list("lŀłȴĺļľƚɫɬᛚᶅᶪḹḻḽⱡꝇꞎꬷꬸ"),
			list("mɱɰɯᵯᶆḿṁṃꬺ𝕞"),
			list("nńņňŉȵɲɳñƞǹṅṇṉṋꞑꞥꬻ"),
			list("oőȱɵòóôõöøōŏơǒǫǭǿȍȏȫȭȯӧөӫ"),
			list("pƥᵱᵽᶈṕṗꝑꝓꝕ𝕡"),
			list("qɋʠꝗꝙ𝕢"),
			list("rŕŗřȑȓɹɍɻɾᶉṙṛṝṟꞧꭉꭊ"),
			list("sšșʂśŝşȿᶊṡṣṥṧṩꞩ"),
			list("tţťŧȶʇʈƫƭțṫᶵṭṯṱᵵẗⱦ𝖙𝕥"),
			list("uũűųȕȗʉùúûüūŭůưǔǖǘǚǜߎ"),
			list("vᶌṽṿⱴⱱꝟ𝕧"),
			list("wŵẁẃẅẇẉẘ𝕨"),
			list("xᶍẋẍꭖꭘꭗꭙ𝓍𝕩"),
			list("yŷȳýÿƴɏʎẏẙỳỵỷỹỿ𝕪"),
			list("zȥɀʐʑźżžƶᵶᶎẑẓẕⱬ𝕫")
		]

		# random character fixers
		new_text = text.replace("\\", "'").replace("''", "'")
		if not speech_marks:
			new_text = new_text.strip('"')
		new_text = new_text.replace("]", ")")
		if "£" in new_text:
			temp = new_text.index("£")
			new_text = new_text[:temp - 1] + new_text[temp:]

		# text formatting
		new_text = self.__formatter(new_text, "G", glitched_letters)

		# names
		if "V{p1_name}" in new_text:
			new_text = self.__word_replacer("V{p1_name}", self.__p1_name, new_text)
		if self.act != 1 and "V{p2_name}" in new_text:
			new_text = self.__word_replacer("V{p2_name}", self.__p2_name, new_text)

		# pronouns
		for (p, q) in self.__p1_pronouns.items():
			new_p = "P1{" + p + "}"
			if new_p in new_text:
				new_text = self.__word_replacer(new_p, q, new_text)
		if self.act != 1:
			for (p, q) in self.__p2_pronouns.items():
				new_p = "P2{" + p + "}"
				if new_p in new_text:
					new_text = self.__word_replacer(new_p, q, new_text)

		return new_text

	def __relation_checker(self, character: str):
		if self.__rel[character] > 0:
			self.__next_bfly_effect = 0
		else:
			self.__next_bfly_effect = 1

	def end_count_updater(self, file: str, ending: str):
		with open(f"memory/{file}.txt", "r") as open_file:
			info = open_file.read().split("\n")
		new_info = ""
		next = False

		for i in info:
			if next:
				new_info += str(int(i) + 1) + "\n"
				next = False
			else:
				new_info += i + "\n"
			if i == ending:
				next = True
		with open(f"memory/{file}.txt", "w") as open_file:
			open_file.write(new_info[:-1])

	# choice functions
	def AAF1(self):
		self.__rel["peter"] -= 2

	def AAK1(self):
		self.__rel["peter"] += 1

	def AAL1(self):
		self.__rel["peter"] += 2

	def AAX1(self):
		self.__rel["gary"] -= 2

	def ABA1(self):
		self.__rel["gary"] -= 5
		self.__items.append("money")

	def ABC1(self):
		self.__rel["gary"] += 2
		self.__items.append("money")

	def ABN1(self):
		self.__relation_checker("gary")

	def ABT1(self):
		self.__gary_knows_name = True

	def ABU1(self):
		self.ABT1()
		self.__rel["gary"] -= 1

	def ABW1(self):
		self.__rel["gary"] -= 3

	def ADP1(self):
		self.end_count_updater("deaths_1", "Death via Idiosy")

	def ADQ1(self):
		self.end_count_updater("deaths_1", "Death via Idleness")

	def ADR1(self):
		self.end_count_updater("deaths_1", '"Alive" via Exploiting PG Requirements')

	def ADS1(self):
		self.end_count_updater("deaths_1", "Death via Volatility")

	def ADT1(self):
		self.end_count_updater("deaths_1", "Death via Vulgarity")

	def ADU1(self):
		self.end_count_updater("deaths_1", "Death via Assholery")

	def ADV1(self):
		self.end_count_updater("deaths_1", "Death via Unluckiness")

	def AEB1(self):
		if "money" in self.__items:
			self.__next_bfly_effect = 0
		else:
			self.__next_bfly_effect = 1

	def AEG1(self):
		self.end_count_updater("deaths_1", "Death via Worthlessness")

	def AEN1(self):
		self.end_count_updater("deaths_1", "Death via Your Ideology")


class Question:
	def __init__(self, code="AAA0"):
		# setting variables
		code = code.replace(",", "")
		self.speaker = g.fetch_db(f"SELECT name FROM Choices WHERE code = '{code}'").strip(",")
		if self.speaker == ":":
			self.speaker = ""
		else:
			self.speaker = g.format(self.speaker) + ":"
		try:
			self.s_col = g.col[g.fetch_db(f"SELECT colour FROM Choices WHERE code = '{code}'").replace(",", "")]
		except:
			self.s_col = g.col["white"]
		self.f = g.fetch_db(f"SELECT function FROM Choices WHERE code = '{code}'").replace(",", "")
		self.questions = {}

		# fetching button name
		if code == "AAA1":
			self.button_text = "NONE"
			self.button_colour = "#ffffff"
		else:
			bt1 = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE choice_codes LIKE '%{code}%'").split(", ")
			bt2 = g.fetch_db(f"SELECT button_codes FROM Choices WHERE choice_codes LIKE '%{code}%'").split(", ")

			# stupid annoying required fix for some reason
			if code == "AAU1":
				bt2[0] = "AAC1"
			elif code == "ABT1":
				bt2[0] = "AAR1"

			try:
				bt3 = bt2[bt1.index(code)]
			except:
				bt3 = bt2[0]

			self.button_text = g.format(g.fetch_db(f"SELECT display_text FROM Buttons WHERE code = '{bt3}'", True))[:-1]
			try:
				self.button_colour = g.col[g.fetch_db(f"SELECT colour FROM Buttons WHERE code = '{bt3}'", True)[:-1]]
			except:
				self.button_colour = g.col["white"]
		temp = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE code = '{code}'").split(", ")
		temp2 = g.fetch_db(f"SELECT button_codes FROM Choices WHERE code = '{code}'").split(", ")
		self.choice_codes = temp
		self.button_codes = temp2

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
		for i in range(len(self.speaker) // 18):
			if self.speaker[-1] != " ":
				break
			self.speaker = self.speaker[:-1]

	def addResponse(self, code: str, q):
		self.questions[code] = q
		
	def addResponses(self, qs):
		for q in qs:
			self.questions[q[0]] = q[1]
			

# generating choice tree
g = GameInfo()
if g.act == 1:
	qtree = Question("AAA1")

# future acts
"""
elif g.act == 2:
	qtree = Question("AAA2")
else:
	qtree = Question("AAA3")
"""