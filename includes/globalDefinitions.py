#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/20/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#

# CURRENCIES
USDT = "USDT"
ETH = "ETH"
BTC = "BTC"
currencies = [USDT, ETH, BTC]

# DEFINE CANDLE FORMAT
CANDLE_FORMAT = {
    # pair:   The chart to which candle belongs.
    "PAIR":     0,
    # date:   Unix timestamp, which represents a certain date and time.
    "DATE":     1,
    # high:   The highest price traded in this candle.
    "HIGH":     2,
    # low:    The lowest price traded in this candle.
    "LOW":      3,
    # open:   The opening price of this candle.
    "OPEN":     4,
    # close:  The closing price of this candle.
    "CLOSE":    5,
    # volume: The total volume that has been traded in this candle.
    "VOLUME":   6
}

# DEFINE INPUT SETTING FORMAT
COMMAND = 0
VARIABLE = 1
VALUE = 2

# DEFINE STATES
INVALID = False
VALID = True
