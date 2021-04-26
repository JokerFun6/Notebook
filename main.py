import sqlite3
from PyQt5 import QtWidgets
import file
import sys
# from db_work import Sql_work


class Application(QtWidgets.QMainWindow, file.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.write_db)
        self.con = sqlite3.connect('film.db')
        self.sql = self.con.cursor()

    def write_db(self):
        title_text = self.title.text()
        genre_text = self.genre.currentText()
        date_text = self.date.text()
        short_inf = self.short_text.toPlainText()
        section_text = self.chapter.currentText()
        lost = (title_text, genre_text, short_inf, int(date_text), section_text)
        db_rec = "INSERT INTO film(title,genre,short_text, date, section) VALUES (?,?,?,?,?)"
        self.sql.execute(db_rec, lost)
        self.con.commit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()  # показывает окно
    app.exec_()  # запускает приложение


main()
