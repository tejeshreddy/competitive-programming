# https://leetcode.com/discuss/interview-question/2337542/Akuna-Capital-2023-Python-Developer-Intern-OA
from ast import arg
from heapq import heapify, heappush, heappop
import datetime

data = [
("2022-03-15", "9:01:00", "Broker", -500, 1500, "2022-04-28", "P", "CBOE", "737acm", "ABC"),
("2022-03-15", "9:00:24", "Electronic", -200, 1500, "2022-04-28", "P", "CBOE", "w6c229", "ABC"),
("2022-03-15", "9:03:45", "Electronic", -100, 1500, "2022-04-28", "P", "CBOE", "tssrin", "ABC"),
("2022-03-15", "9:00:53", "Electronic", -500, 1500, "2022-04-28", "P", "CBOE", "lk451a", "XYZ"),
("2022-03-15", "9:00:05", "Electronic", -350, 1500, "2022-04-28","C", "CBOE", "9numpr", "ABC"),
("2022-03-15", "9:00:35", "Electronic", 200, 1500, '2022-04-28', "P", "CBOE", "922v3g", "ABC"),
("2022-03-15", "9:00:47", "Electronic", -150, 1500, "2022-04-21", "P", "CBOE", "bg54nm", "ABC"),
("2022-03-15", "9:02:23", "Electronic", -200, 1550, "2022-04-28", "P", "CBOE", "6y7fhm", "ABC")
]


class Trade:
    def __init__(self, type, qty, strike, expiry, kind, exchange, trade_id, product):
        self.type = type
        self.qty = qty
        self.strike = strike
        self.expiry = expiry
        self.kind =  kind
        self.exchange = exchange
        self.trade_id = trade_id
        self.product = product

def show_trade(bt, et):
    print(bt.product, et.product)
    print(bt.type, et.type)
    print(bt.qty, et.qty)
    print(bt.expiry, et.expiry)
    print(bt.strike, et.strike)

def validate_trade(bt, et):
    if bt.product == et.product and ((bt.qty > 0 and et.qty > 0) or (bt.qty < 0 and et.qty < 0)) and bt.expiry == et.expiry and bt.strike == et.strike:
        return True
    return False

front_running_trades = []
electronic_trades, broker_trades = [], []


for trade in data:
    print(trade)
    date_string = trade[0] + " " + trade[1]
    dt = int(datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime("%s"))

    if trade[2] == "Electronic":    
        heappush(electronic_trades, (dt, Trade(*trade[2:])))
    else:
        heappush(broker_trades, (dt, Trade(*trade[2:])))

while broker_trades:
    broker_timestamp, broker_trade = heappop(broker_trades)

    for i in range(len(electronic_trades)):
        electronic_timestamp, electronic_trade = electronic_trades[i]

        if broker_timestamp - electronic_timestamp <= 60 and validate_trade(broker_trade, electronic_trade):
            show_trade(broker_trade, electronic_trade)
            front_running_trades.append((broker_trade.trade_id, electronic_trade.trade_id))
            print("\n")

print(front_running_trades)










