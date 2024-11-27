import sqlite3

connector = sqlite3.connect("choice_tree.db")
sql = connector.cursor()

def run_sql(file: str):
    with open(file + ".sql", "r") as filey:
        code = filey.read()

    for c in code.split(";"):
        sql.execute(c + ";")

run_sql("table_creator")
run_sql("choices_editor")
run_sql("buttons_editor")