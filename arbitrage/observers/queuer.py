import json
import logging
import datetime
import pymongo
from .observer import Observer

from pymongo import MongoClient
client = MongoClient()
db = client.ng_bitcoin_arbitrage

class Queuer(Observer):
    db = None

    def begin_opportunity_finder(self, depths):
        logging.info("begin finder")

    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid, perc,
                    weighted_buyprice, weighted_sellprice):
        logging.info("profit: %f USD with volume: %f BTC - buy at %.4f (%s) sell at %.4f (%s) ~%.2f%%" % (profit, volume, buyprice, kask, sellprice, kbid, perc))
        
        # TODO: invalidate an opportunity after the price changes
        db.opportunities.update({"kbid" : kbid, "kask" : kask}, {
            "profit" : profit,
            "volume" : volume,
            "buyprice" : buyprice,
            "kask" : kask,
            "sellprice" : sellprice,
            "kbid" : kbid,
            "perc" : perc,
            "weighted_buyprice" : weighted_buyprice,
            "weighted_sellprice" : weighted_sellprice,
            "updated_on" : datetime.datetime.utcnow()
        }, upsert=True)

