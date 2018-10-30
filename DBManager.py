import pymongo
import datetime
import Scraper


def getDB(): # connect to mongodb
    client = pymongo.MongoClient('localhost:27017')

    db = client.BitBotTest

    return db

def addEntry(db): # add new data
    # request data
    [name, usdPrice, eurPrice, percentChange7d, percentChange24h, percentChange1h,lastUpdated] = Scraper.getNewData()

    # insert on DB
    db.test.insert({"name" : name,
                    "usdPrice" : usdPrice,
                    "eurPrice" : eurPrice,
                    "percentChange7d" : percentChange7d,
                    "percentChange24h" : percentChange24h,
                    "percentChange1h" : percentChange1h,
                    "date" : datetime.datetime.fromtimestamp(int(lastUpdated)).strftime('%Y-%m-%d %H:%M:%S')})

def getEntries(db): # print all data
    for data in db.test.find():
        print(data)
