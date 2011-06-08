import sys
from PySide.QtGui import QMessageBox
from PySide.QtSql import *

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("testdb")
if not db.open():
    QMessageBox.warning(None, "Phone Log",
                        "Database Error")
    sys.exit(1)

query = QSqlQuery()
query.exec_("""CREATE TABLE outcomes (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR(40) NOT NULL)""")

query.exec_("""CREATE TABLE calls (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                caller VARCHAR(40) NOT NULL,
                starttime DATETIME NOT NULL,
                endtime DATETIME NOT NULL,
                topic VARCHAR(80) NOT NULL,
                outcomeid INTEGER NOT NULL,
                FOREIGN KEY (outcomeid) REFERENCES outcomes)""")
