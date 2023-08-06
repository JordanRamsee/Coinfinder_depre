from icons import *
from activate import *
import threading
from flaskapp import app
import os
import ccxt

class CrossTask:
    def __init__(self, taskId, exchanges, currencypairs):
        self.id = taskId
        self.exchanges = exchanges
        self.currencypairs = currencypairs

    def get_pairs(self):
        for exchange in ccxt.exchanges:
            try:          
                inst = getattr(ccxt, exchange)()
                markets = inst.load_markets()

                print("PAIR COUNT: " + str(len(markets)))
                for m in markets:
                    print(m)
            except:
                pass

    def get_bid_ask(self):
        for exchanges in self.exchanges:
            try:
                for exchange in exchanges:
                    for symbol in self.currencypairs:
                        orderbook = exchange.fetch_order_book(symbol)
            except:
                pass
    
    def get_balance(self):
        try:
            binance = ccxt.binance(config={
                'apiKey': '',
                'secret': '',
                'enableRateLimit': True,
            })
            print(binance.fetch_balance()['info']['positions'])
        except:
            pass