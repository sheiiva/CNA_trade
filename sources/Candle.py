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


import sources.include as globals
from sources.Rate import Rate


class Candle():
    """
    A candlestick chart is a style of financial chart used to describe
    price movements of a security, derivative, or currency.
    """

    def __init__(self, inputCandle: str):
        self._state = globals.VALID
        self._rates = self.initRates(inputCandle)

    def initRates(self, inputCandle: str) -> list:
        """
        Parse the inputCandle string into a list of three `rates`.

        Args:
            inputCandle (str): the input command to be parsed.

        Returns:
            list: such as [Rate, Rate, Rate]
        """

        # Split input string (cut by a semi-colon)
        inputsRate = inputCandle.split(sep=";")
        if len(inputsRate) is not 3:
            # print("INPUT ERROR: might be three rates per candle.")
            return None

        outputRates = [Rate(inputsRate[0]), Rate(inputsRate[1]), Rate(inputsRate[2])]
        # Check for rates' validity
        for rate in outputRates:
            if rate._state is globals.INVALID:
                # print("ERROR: candle is invalid")
                self._state = globals.INVALID
        return outputRates
