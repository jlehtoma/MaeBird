import sys
from PySide.QtCore import QDateTime
from PySide.QtGui import QMessageBox
from PySide.QtSql import *

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("linnutFIN.sqlite")
if not db.open():
    QMessageBox.warning(None, "Error",
                        "Database Error")
    sys.exit(1)

query = QSqlQuery()

def create_observations():
    
    print("Dropping table...")
    query = QSqlQuery()
    query.exec_("DROP TABLE observations")
    
    print("Creating table...")
    query.exec_("""CREATE TABLE observations (
                ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                SPECIES INTEGER NOT NULL,
                ABBR INTEGER NOT NULL,
                COUNT INTEGER,
                TIME DATETIME NOT NULL,
                LOCATION VARCHAR(80) NOT NULL,
                NOTES VARCHAR(180) NOT NULL)""")
    if query.lastError():
        print query.lastError().text()

def populate_observations(data):

    query.prepare("INSERT INTO observations (SPECIES, ABBR, COUNT, TIME, "
                  "LOCATION, NOTES) VALUES (?, ?, ?, ?, ?, ?)")
    for species, abbr, count, time, location, notes in data:
        query.addBindValue(species)
        query.addBindValue(abbr)
        query.addBindValue(count) # QDateTime
        query.addBindValue(time)   # QDateTime
        query.addBindValue(location)
        query.addBindValue(notes) # int
        query.exec_()

DATETIME_FORMAT = "dd.MM.yyyy hh:mm"
data = [[10,
         10,
         5, 
         QDateTime.currentDateTime(),
         "Herttoniemi",
         "Hieno!"],
         [4,
          4,
          100,
          QDateTime.currentDateTime(),
          "62.12414 38.214124",
          "Ei niin hieno"]
         ]
create_observations()
populate_observations(data)