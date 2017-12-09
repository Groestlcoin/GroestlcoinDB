import subprocess
import json

def getNewData():

    # create variables
    [name, usdPrice, brlPrice, percentChange7d, percentChange24h, percentChange1h,lastUpdated] = [None, None, None, None, None, None, None]

    # request data
    actualInfo = subprocess.getoutput("curl -s https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=BRL")

    jdata = json.loads(actualInfo) # convert to json

    for data in jdata: # print all elements, from all jsons
        for key, value in data.items():
            # get json information and put on variables
            if(key == "id"):
                name = value

            elif(key == "price_usd"):
                usdPrice = value

            elif(key == "price_brl"):
                brlPrice = value

            elif(key == "percent_change_7d"):
                percentChange7d = value

            elif(key == "percent_change_24h"):
                percentChange24h = value

            elif(key == "percent_change_1h"):
                percentChange1h = value

            elif(key == "last_updated"):
                lastUpdated = value


    return [name, usdPrice, brlPrice, percentChange7d, percentChange24h, percentChange1h,lastUpdated]
