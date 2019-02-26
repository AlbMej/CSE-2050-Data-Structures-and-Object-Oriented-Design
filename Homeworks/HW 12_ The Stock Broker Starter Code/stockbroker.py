from priorityqueue import *

class Request:
    def __init__(self, price, share):
        self.price = price
        self.share = share
        
    def __eq__(self, other):
        return self.price == other.price and self.share == other.share
    
class Broker:
    # implement this method
    def __init__(self, bids, asks):
        self.bids = PriorityQueue(bids, lambda x: -x.price)
        self.asks = PriorityQueue(asks, lambda x: x.price)
        self.last_trade = (0,0,1) #(highest bid , lowest ask, shares bought)
        self.trades =[]
        self.profit = 0

    # implement this method
    def trade(self):
        highest_bid = self.bids.findtop()
        lowest_ask = self.asks.findtop()
        trade = None
        if highest_bid.price >= lowest_ask.price: 
            bid_shares = self.bids.findtop().share
            ask_shares = self.asks.findtop().share

            if bid_shares == ask_shares: 
                highest_bid = self.bids.removetop()
                lowest_ask = self.asks.removetop()
                self.last_trade = (highest_bid, lowest_ask, bid_shares)
                trade = (highest_bid, lowest_ask)
                self.profit += int((self.last_trade[0].price - self.last_trade[1].price) * self.last_trade[2])
            
            elif bid_shares > ask_shares:
                lowest_ask = self.asks.removetop()
                self.bids._entries[0].share = bid_shares - ask_shares
                self.last_trade = (highest_bid, lowest_ask, ask_shares)
                trade = (Request(highest_bid.price, ask_shares), lowest_ask)
                self.profit += int((self.last_trade[0].price - self.last_trade[1].price) * self.last_trade[2])

            else: #ask share > bid shares
                highest_bid = self.bids.removetop()
                self.asks._entries[0].share = ask_shares - bid_shares
                self.last_trade = (highest_bid, lowest_ask, bid_shares) #All shares wanted are bought
                trade = (highest_bid, Request(lowest_ask.price, bid_shares))
                self.profit += int((self.last_trade[0].price - self.last_trade[1].price) * self.last_trade[2])
        return trade

    # implement this method
    def tradeall(self):
        highest_bid = self.bids.findtop()
        lowest_ask = self.asks.findtop()
        trades = []
        while highest_bid.price >= lowest_ask.price: 
            trades.append(self.trade())
            highest_bid = self.bids.findtop()
            lowest_ask = self.asks.findtop()
        return trades

    # implement this method
    def getprofit(self):
        return self.profit
