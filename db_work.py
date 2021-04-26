import sqlite3


class Sql_work():
    def __init__(self):
        self.con = sqlite3.connect('film.db')
        self.sql = self.con.cursor()
        self.default_status = 'В планах'

    def record(self, title, genre, date ,short_text,section):
        self.sql.execute(f"INSERT INTO film_list VALUES (?,?,?,?,?,?)",
                    (title, genre, short_text, date, section))
        self.con.commit()
