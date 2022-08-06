# https://leetcode.com/discuss/interview-question/2337542/Akuna-Capital-2023-Python-Developer-Intern-OA
from ast import arg
from heapq import heapify, heappush, heappop
import datetime

data = [
("2022-03-15", "9:01:00", "Broker", -500, 1500, "202204-28", "P", "CBOE", "737acm", "ABC"),
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



all_trades = []
for trade in data:
    epoch = datetime.datetime(trade[0] + " " + trade[1]).strftime("")
    all_trades.append(Trade(*trade[2:]))

