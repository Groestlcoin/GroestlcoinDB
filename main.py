import DBManager
import time

db = DBManager.getDB()

while (1):
    DBManager.addEntry(db)
    time.sleep(600) # wait 10 min
