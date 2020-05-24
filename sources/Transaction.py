#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/23/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#


import numpy as np

import includes.globalDefinitions as globals
from sources.utils.Logger import Logger
from sources.Candle import Candle
from sources.Rate import Rate
from sources.Stack import Stack

class Transaction:

    def __init__(self):
        self._n = 20 # Default value for average computation
        self._n_lastClosePrices = []

    def isValidCurrency(self, inputCurrency: str) -> bool:
        """
        Check if `inputCurrency` is a valid currency.

        Args:
            inputCurrency (str): The currency to be checked.

        Returns:
            bool: True if `inputCurrency` is a valid currency. False otherwise.
        """

        if inputCurrency in globals.currencies:
            return True
        return False

    def no_moves(self):
        """
        Don't take any position.
        """

        print("no_moves")

    def buy(self, currencyPaidWith: str, currencyReceived: str, amount: int):
        """
        Buy `amount` of `currencyReceived` in `currencyPaidWith`.

        Args:
            currencyPaidWith (str): Input currency of the transaction.
            currencyReceived (str): Output currency of the transaction.
            amount (int): Specifies how much to buy.
        """


        if self.isValidCurrency(currencyPaidWith) is False\
        or self.isValidCurrency(currencyReceived) is False:
            Logger("Wrong currencies for buying transaction.")
        else:
            print("buy {}_{} {}".format(currencyPaidWith, currencyReceived, amount))

    def sell(self, currencyReceived: str, currencySold: str, amount: int):
        """
        Sell `amount` of `currencySold` in `currencyReceived`.

        Args:
            currencyReceived (str): Ouput currency of the transaction.
            currencySold (str): Input currency of the transaction.
            amount (int): Specifies how much to sell.
        """

        if self.isValidCurrency(currencyReceived) is False\
        or self.isValidCurrency(currencySold) is False:
            Logger("Wrong currencies for selling transaction.")
        else:
            print("sell {}_{} {}".format(currencyReceived, currencySold, amount))

    def getLastNClosingPrices(self, candles: list) -> list:
        """
        Get the last `self._n` closing prices from input candles.

        Args:
            candles (list): The sources candles.
        Returns:
            list: A list containing the last `self._n` closing prices.
        """
 
        def getClosingPrices(candle: Candle, rate: int) -> float:
            if rate >= 0 and rate <= 2:
                return candle._rates[rate]._close
            return 0.

        ret = [[], [], []]

        for candle in candles:
            for i in range(3):
                ret[i].append(getClosingPrices(candle, i))

        return [last[-self._n:] for last in ret]

    def computeSimpleMeanAverage(self) -> int:
        """
        Compute a Simple Mean Average (SMA) of the last `._n` closing prices.

        Returns:
            int: The Simple Mean Average (SMA).
        """

        return [sum(line)/len(line) for line in self._n_lastClosePrices]

    def comput_standarDeviation(self) -> int:
        """
        Compute a Standard Deviation (std) of the last `._n` closing prices.

        Returns:
            int: The standard deviation (std).
        """

        return [np.std(line) for line in self._n_lastClosePrices]

    def strategy(self, candles: Candle, stack: Stack):

        sma = self.computeSimpleMeanAverage()
        std = self.comput_standarDeviation()

        def isInUpperBand(value: float) -> bool:
            if value <= (sma + (2 * std)) and value >= (sma + std):
                return True
            return False
        
        def isInLowerBand(value: float) -> bool:
            if value >= (sma - (2 * std)) and value <= (sma + std):
                return True
            return False

        # for i in range(len(globals.currencies)):
        if isInUpperBand(candles[-1]._rates[0]._close): # replace 0 with currency to check
            self.buy(globals.currencies[0], globals.currencies[1], 1)
        elif isInLowerBand(candles[-1]._rates[0]._close): # replace 0 with currency to check
            self.sell(globals.currencies[0], globals.currencies[1], 1)
        else:
            self.no_moves()