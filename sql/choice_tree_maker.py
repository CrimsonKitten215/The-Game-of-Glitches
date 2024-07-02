import sqlite3

connector = sqlite3.connect("choice_tree.db")
sql = connector.cursor()

with open("sql.txt", "r") as file:
    code = file.read()

for c in code.split(";"):
    sql.execute(c + ";")