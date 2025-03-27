import random
import sqlite3
import useful_code.type_convertor as tc

class GameInfo:
	"""
	Class that stores all the game's variables and the functions for events in the game that change them.
	"""
	def __init__(self):
		# sql
		connector = sqlite3.connect("sql/choice_tree.db")
		self.__sql = connector.cursor()

		# colours
		self.col = {
			"mia": "#ff0000",
			"mia_stressed": "#887777",
			"mia_angry": "#00ffff",
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
			"gold": "#db901c"
		}

		# relationship levels
		self._rel = {
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
		self.__act = int(info[1])
		if self.__act != 1:
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
		self.transgenderfy(info[3], 1)
		self.transgenderfy(info[7], 2)

		# single-playthrough variables
		self._next_bfly_effect = 0
		self._items = []
		self._recent_end = "none"
		self._gary_name_version = ["whatever P1{their} name was", "no-name"]

	# getters/setters
	def get_p1_name(self):
		return self.__p1_name

	def get_p2_name(self):
		return self.__p2_name

	def get_items(self):
		return self._items

	def get_act(self):
		return self.__act

	def get_gary_name_version(self):
		return self._gary_name_version

	def _set_gary_name_version(self, new):
		self._gary_name_version = new

	def _set_items(self, new: list):
		self._items = new

	def _set_next_bfly_effect(self, new: int):
		self._next_bfly_effect = new

	def _set_col(self, new: dict):
		self.col = new

	def _set_rel(self, new: dict):
		self._rel = new

	def set_p1_name(self, new: str):
		self.__p1_name = new

	def set_p2_name(self, new: str):
		self.__p2_name = new

	def set_act(self, new: int):
		self.__act = new

	# basic functions
	def __get_value(self, q, text: str):
		try:
			return getattr(self, text)
		except:
			return getattr(q, text)

	def get_info(self, q):
		text = ""
		with open(f"save_slots/slot_default.txt", "r") as file:
			info = file.read().split("\n")

		for i in range(0, len(info), 2):
			text += "\n" + info[i] + "\n"
			line = self.__get_value(q, info[i])
			if isinstance(line, list):
				text += tc.unlistify(line)
			elif isinstance(line, dict):
				text += tc.undictify(line)
			else:
				text += str(line).replace("\n", "/n")

		return text[1:]

	def set_info(self, q, info: list):
		for i in range(0, len(info), 2):
			# setting temp variables
			var = self.__get_value(q, info[i])
			try:
				f = getattr(self, "_set_" + info[i].strip("_"))
			except:
				f = getattr(q, "set_" + info[i].strip("_"))

			# checking if correct type
			if isinstance(var, list):
				f(tc.listify(info[i + 1]))
			elif isinstance(var, dict):
				f(tc.dictify(info[i + 1]))
			elif isinstance(var, bool):
				f(info[i + 1] == "True")
			elif isinstance(var, int):
				f(int(info[i + 1]))
			elif isinstance(var, float):
				f(float(info[i + 1]))
			else:
				f(info[i + 1].replace("/n", "\n"))
		q.questions = {}
		return q

	def transgenderfy(self, gender: str, player: int):
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
				question.choice_codes = [question.choice_codes[self._next_bfly_effect]]
			for c in question.choice_codes:
				question.add_response(c, Question(c))

	@staticmethod
	def __word_replacer(old_word: str, new_word: str, text: str):
		while old_word in text:
			temp = text.index(old_word)
			if temp == 0:
				text = new_word + text[len(old_word):]
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

			for c in new_text[start + 2: end]:
				if c in alphabet:
					loc = alphabet.index(c)
					temp += new_alpha[loc][random.randint(0, len(new_alpha[loc]) - 1)]
				else:
					temp += c

			new_text = self.__word_replacer(new_text[start: end] + "}", temp, new_text)
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
		'': '
		,,: ;
		"""

		# glitched alphabet
		glitched_letters = [
			list("AĀĂĄȀȂȦÀÁÃÄÅǍǞǠǺȺӐӒΆἈἉἊἋἌἍἎἏᾈᾉᾊᾋᾌᾍᾎᾏᾸᾹᾺΆᾼ"),
			list("BƁƂɃᛒḂḄḆ"),
			list("CĆĈƇʗℂÇĊČḈℭꞒꜾ"),
			list("DĐƉⅅĎƊḊḌḎḐḒ"),
			list("EĒĔĖĘȄȆȨɆÈÉÊËĚƎ"),
			list("FƑℲḞꞘꟻ"),
			list("GĠĢƓ⅁ĜĞǤǦǴḠ𝔾𝕲"),
			list("HĤĦȞᚻᚺḢḤḦḨḪℌℍⱧꞪＨ𝓗"),
			list("IĨİƗȈÌÍÎÏĪĬĮǏȊ"),
			list("JĴ𝔍𝕁𝒥"),
			list("KĶƘKǨḰḲḴⱩꝀꝂꝄꞢꞰ𝒦𝓚𝕂"),
			list("LĹŁĽĻĿḶḸḺḼⱠⱢꝆꝈ"),
			list("MℳḾṀṂⱮꟽ𝓜𝔐𝕄"),
			list("NŃŅŇȠℕÑƝǸṄṆṈṊ∏⋂ꞤꞐ"),
			list("OŐȰÒÓÔÕÖØŌŎƟƠǑǪǬǾȌȎȪȬȮӦӨӪ"),
			list("PℙƤṔṖⱣꝐꝒꝔꟼ𝓟"),
			list("QɊℚ℺ꝘꝖ𝒬"),
			list("RŔŖŘȐȒɌᚱṘṚṜⱤℝℜṞꝚꞦ"),
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
			list("cćĉƈɕↄçċčȼḉꜿꞓ"),
			list("dđȡɖɗƌďᶑᶁᵭḋḍḏḑḓ"),
			list("eēĕėęȅȇȩɇɘèéêëěǝ"),
			list("fƒᵮᶂḟ"),
			list("gġģɠĝğǥǧǵᶃᵷḡꞡ"),
			list("hĥħɦȟḣḥḧḩḫẖⱨ𝕙"),
			list("iĩıȉɨìíîïīĭįǐȋ"),
			list("jĵȷɉĵǰɟʝ𝕛"),
			list("kķƙǩʞḱᶄḳⱪḵꝁꝃꝅꞣ𝕜"),
			list("lŀłȴĺļľƚɫɬᛚᶅᶪḹḻḽⱡꝇꞎ"),
			list("mɱɰɯᵯᶆḿṁṃ𝕞"),
			list("nńņňŉȵɲɳñƞǹṅṇṉṋꞑꞥ"),
			list("oőȱɵòóôõöøōŏơǒǫǭǿȍȏȫȭȯӧөӫ"),
			list("pƥᵱᵽᶈṕṗꝑꝓꝕ𝕡"),
			list("qɋʠꝗꝙ𝕢"),
			list("rŕŗřȑȓɹɍɻɾᶉṙṛṝṟꞧ"),
			list("sšșʂśŝşȿᶊṡṣṥṧṩꞩ"),
			list("tţťŧȶʇʈƫƭțṫᶵṭṯṱᵵẗⱦ𝖙𝕥"),
			list("uũűųȕȗʉùúûüūŭůưǔǖǘǚǜߎ"),
			list("vᶌṽṿⱴⱱꝟ𝕧"),
			list("wŵẁẃẅẇẉẘ𝕨"),
			list("xᶍẋẍ𝓍𝕩"),
			list("yŷȳýÿƴɏʎẏẙỳỵỷỹỿ𝕪"),
			list("zȥɀʐʑźżžƶᵶᶎẑẓẕⱬ𝕫")
		]

		# random character fixers
		new_text = text.replace("''", "'").replace("\\'", "'").replace(",,", ";")
		if not speech_marks:
			new_text = new_text.strip('"')
		new_text = new_text.replace("[", "(")
		new_text = new_text.replace("]", ")")

		# variables (change later)
		while "V{" in new_text:
			start_i = new_text.find("V{")
			for i in range(start_i, len(new_text)):
				if new_text[i] != "}":
					continue

				variable = new_text[start_i + 2 : i]
				if variable[-1] == "]":
					proper_word = getattr(g, "get_" + variable[:variable.index("[") - 1])()
					if isinstance(proper_word, list):
						proper_word = proper_word[int(variable[variable.index("[") + 1 : -2])]
				else:
					proper_word = getattr(g, "get_" + variable)()

				new_text = self.__word_replacer(new_text[start_i : i + 1], proper_word, new_text)
				break

		# pronouns
		for (p, q) in self.__p1_pronouns.items():
			new_p = "P1{" + p + "}"
			if new_p in new_text:
				new_text = self.__word_replacer(new_p, q, new_text)
		if self.__act != 1:
			for (p, q) in self.__p2_pronouns.items():
				new_p = "P2{" + p + "}"
				if new_p in new_text:
					new_text = self.__word_replacer(new_p, q, new_text)

		# text formatting
		new_text = self.__formatter(new_text, "G", glitched_letters)

		return new_text

	def __relation_checker(self, character: str):
		if self._rel[character] > 0:
			self._next_bfly_effect = 0
		else:
			self._next_bfly_effect = 1

	@staticmethod
	def __end_count_updater(file: str, ending: str, amount=1):
		with open(f"memory/{file}.txt", "r") as open_file:
			info = open_file.read().split("\n")
		new_info = ""
		next = False

		for i in info:
			if next:
				new_info += str(int(i) + amount) + "\n"
				next = False
			else:
				new_info += i + "\n"
			if i == ending:
				next = True
		with open(f"memory/{file}.txt", "w") as open_file:
			open_file.write(new_info[:-1])

	@staticmethod
	def __recolour(col: str, amount: int, num: int):
		hex = "0123456789abcdef"
		col = "#" + (2 * hex[hex.find(col[1]) - num]) + (4 * hex[hex.find(col[3]) + num])
		return col, amount - num

	def __update_mia_colour(self, amount: int):
		self._rel["mia"] -= amount
		col = self.col["mia"]

		while amount != 0 and not ((amount < 0 and col == "#ff0000") or (amount > 0 and col == "#00ffff")):
			if amount > 0:
				col, amount = self.__recolour(amount, 1)
			else:
				col, amount = self.__recolour(amount, -1)

		self.col["mia"] = col

	def __change_bfly_effect(self, requirement: bool):
		"""
		Changes the next butterfly effect to 0 if th requirement is met.
		:param requirement: Requirement for it to be 0
		"""
		if requirement:
			self._next_bfly_effect = 0
		else:
			self._next_bfly_effect = 1

	def __path_randomiser(self, chance: int, out_of: int):
		"""
		Makes the path the player goes down random.
		:param chance: Numerator of the fractional probability of it being 0
		:param out_of: Denominator of the fractional probability of it being 0
		"""
		r = random.randint(0, out_of - 1)
		self.__change_bfly_effect(r < chance)

	# choice functions
	def na(self):
		pass

	def AAF1(self):
		self._rel["peter"] -= 2

	def AAK1(self):
		self._rel["peter"] += 1

	def AAL1(self):
		self._rel["peter"] += 2

	def AAX1(self):
		self._rel["gary"] -= 2

	def ABA1(self):
		self._rel["gary"] -= 5
		self._items.append("money")

	def ABC1(self):
		self._rel["gary"] += 2
		self._items.append("money")

	def ABN1(self):
		self.__relation_checker("gary")

	def ABT1(self):
		self._gary_name_version = self.__p1_name

	def ABU1(self):
		self.ABT1()
		self._rel["gary"] -= 1

	def ABW1(self):
		self._rel["gary"] -= 3

	def ADP1(self):
		self.__end_count_updater("deaths_1", "Death via Idiocy")

	def ADQ1(self):
		self.__end_count_updater("deaths_1", "Death via Idleness")

	def ADR1(self):
		self.__end_count_updater("deaths_1", '"Alive" via Exploiting PG Requirements')

	def ADS1(self):
		self.__end_count_updater("deaths_1", "Death via Volatility")

	def ADT1(self):
		self.__end_count_updater("deaths_1", "Death via Vulgarity")

	def ADU1(self):
		self.__end_count_updater("deaths_1", "Death via Assholery")

	def ADV1(self):
		self.__end_count_updater("deaths_1", "Death via Unluckiness")

	def AEB1(self):
		self.__change_bfly_effect("money" in self._items)

	def AEG1(self):
		self.__end_count_updater("deaths_1", "Death via Worthlessness")

	def AEN1(self):
		self.__end_count_updater("deaths_1", "Death via Your Ideology")

	def AEW1(self):
		self.__end_count_updater("deaths_1", "Death via Spooning")

	def AFC1(self):
		self.__end_count_updater("deaths_1", "Death via Taunting")

	def AFM1(self):
		self.__update_mia_colour(2)

	def AFN1(self):
		self.__update_mia_colour(4)

	def AFR1(self):
		self.__end_count_updater("deaths_1", "Death via Lead Poisoning")

	def AGB1(self):
		self.__end_count_updater("deaths_1", "Death via The Matrix (green)")

	def AGD1(self):
		self.__end_count_updater("deaths_1", "Death via The Matrix (yellow)")

	def AGF1(self):
		self.__end_count_updater("deaths_1", "Death via Drug Overdose", 10)

	def AGS1(self):
		self.__end_count_updater("deaths_1", "Death via Not Keeping Away from Children", 1)

	def AHX1(self):
		self._rel["gary"] += 3
		self._rel["ryan"] += 1

	def AHS1(self):
		self.__end_count_updater("deaths_1", "Death via Vacuousness", 1)

	def AIC1(self):
		self.__path_randomiser(1, 4)


class Question:
	def __init__(self, code="AAA0"):
		code2 = code.replace(",", "")

		# duplicate checker
		if int(code2[-1]) > 4:
			c = code2[:3]
			temp = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE choice_codes LIKE '%{code2}%' AND choice_codes LIKE '{c}%'")
			self.code = c + temp[temp.index(c) + 3]
		else:
			self.code = code2

		self.speaker = g.fetch_db(f"SELECT name FROM Choices WHERE code = '{self.code}'").strip(",")
		if self.speaker == ":":
			self.speaker = ""
		else:
			self.speaker = g.format(self.speaker) + ":"
		try:
			self.s_col = g.col[g.fetch_db(f"SELECT colour FROM Choices WHERE code = '{self.code}'").replace(",", "")]
		except:
			self.s_col = g.col["white"]
		self.f = g.fetch_db(f"SELECT function FROM Choices WHERE code = '{self.code}'").replace(",", "")
		self.questions = {}

		# fetching button name
		if self.code == "AAA1":
			self.button_text = "NONE"
			self.button_colour = "#ffffff"
		else:
			bt1 = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE choice_codes LIKE '%{code2}%'").split(", ")
			bt2 = g.fetch_db(f"SELECT button_codes FROM Choices WHERE choice_codes LIKE '%{code2}%'").split(", ")
			try:
				bt3 = bt2[bt1.index(code2)]
			except:
				bt3 = bt2[0]

			self.button_text = g.format(g.fetch_db(f"SELECT display_text FROM Buttons WHERE code = '{bt3}'", True))[:-1]
			if self.button_text[0] == '"' and self.button_text[-1] != '"':
				self.button_text = self.button_text[1:]
			try:
				self.button_colour = g.col[g.fetch_db(f"SELECT colour FROM Buttons WHERE code = '{bt3}'", True)[:-1]]
			except:
				self.button_colour = g.col["white"]

		temp = g.fetch_db(f"SELECT choice_codes FROM Choices WHERE code = '{self.code}'").split(", ")
		temp2 = g.fetch_db(f"SELECT button_codes FROM Choices WHERE code = '{self.code}'").split(", ")
		self.choice_codes = temp
		self.button_codes = temp2

		# aligning text
		self.question = ""
		temp_q = g.format(g.fetch_db(f"SELECT speech FROM Choices WHERE code = '{self.code}'", True)[:-1].replace("\\n", "⟗"), False)
		if len(temp_q) > 100 and "⟗" not in temp_q:
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
			self.question = temp_q.replace("\⟗", "\n")

		if len(self.speaker) < len(self.question):
			lines = self.question.split("\n")
			max = 0
			for l in lines:
				if len(l) > max:
					max = len(l)
			self.speaker += " " * (max - len(self.speaker))

	def add_response(self, code: str, q):
		self.questions[code] = q
		
	def add_responses(self, qs):
		for q in qs:
			self.questions[q[0]] = q[1]

	# getters/setters
	def get_game_info(self):
		return g.get_info(self)

	def set_game_info(self, info: list):
		return g.set_info(self, info)

	def set_code(self, new: str):
		self.code = new

	def set_f(self, new: str):
		self.f = new

	def set_button_text(self, new: str):
		self.button_text = new

	def set_button_colour(self, new: str):
		self.button_colour = new

	def set_speaker(self, new: str):
		self.speaker = new

	def set_s_col(self, new: str):
		self.s_col = new

	def set_choice_codes(self, new: list):
		self.choice_codes = new

	def set_button_codes(self, new: list):
		self.button_codes = new

	def set_question(self, new: str):
		self.question = new

# generating choice tree
g = GameInfo()
act = g.get_act()

# act 1 survey
if act == 0:
	qtree = Question("AAB0")
# act 2 survey
elif act == 4:
	qtree = Question("AAE0")
# acts without the survey
else:
	qtree = Question("AAA" + str(act))