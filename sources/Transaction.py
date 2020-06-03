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
        self._period = 20  # Default value for average computation
        # TO NOTE: [BTC_ETH, USDT_ETH, USDT_BTC] (in order)
        self._period_lastClosePrices = [[], [], []]

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

    def update_lastClosePrices(self, candle: Candle) -> None:
        for i in range(len(self._period_lastClosePrices)):
            self._period_lastClosePrices[i].append(candle._rates[i]._close)
            # Keep only the `._period` last.
            self._period_lastClosePrices[i] = self._period_lastClosePrices[i][-self._period:]

    def computeSimpleMeanAverage(self, values: list) -> int:
        """
        Compute the average of the list's values.

        Args:
            values (list): Input list.

        Returns:
            int: Average of list's values.
        """
        if len(values) is 0:
            return 0
        return sum(values)/len(values)

    def comput_standarDeviation(self, values: list) -> int:
        """
        Compute the standard deviation of the list's values.

        Args:
            values (list): Input list.

        Returns:
            int: Standard deviation of list's values.
        """
        return np.std(values)

    def no_moves(self):
        """
        Don't take any position.
        """

        print("pass")

    def buy(self, currencyPaidWith: str, currencyReceived: str, amount: int):
        """
        Buy `amount` of `currencyReceived` in `currencyPaidWith`.

        Args:
            currencyPaidWith (str): Input currency of the transaction.
            currencyReceived (str): Output currency of the transaction.
            amount (int): Specifies how much to buy.
        """

        print("buy {}_{} {}".format(currencyPaidWith,
                                    currencyReceived,
                                    amount), end='')

    def sell(self, currencyReceived: str, currencySold: str, amount: int):
        """
        Sell `amount` of `currencySold` in `currencyReceived`.

        Args:
            currencyReceived (str): Ouput currency of the transaction.
            currencySold (str): Input currency of the transaction.
            amount (int): Specifies how much to sell.
        """

        print("sell {}_{} {}".format(currencyReceived,
                                     currencySold,
                                     amount), end='')

    def transaction(self, currencyIn: str, currencyOut: str,
                            moneyIn: float, moneyOut: float,
                            candles: list, pastAction: bool) -> bool:
        """
        Decide to buy, sell or pass.

        Args:
            currencyIn (str): The input currency of the transaction.
            currencyOut (str): The output currency of the transaction.
            moneyIn (float): The stack of the input currency.
            moneyOut (float): The stack of the output currency.
            candles (list): List of the registered candles.
            pastAction (bool): True if has already bought something.

        Returns:
            bool: True if has bought something, False otherwise.
        """
        def fetchClosePrices(currencyIn: str, currencyOut: str) -> list:
            if f"{currencyIn}_{currencyOut}" == "BTC_ETH":
                return self._period_lastClosePrices[0]
            elif f"{currencyIn}_{currencyOut}" == "USDT_ETH":
                return self._period_lastClosePrices[1]
            elif f"{currencyIn}_{currencyOut}" == "USDT_BTC":
                return self._period_lastClosePrices[2]

        # Get `._period` last close prices of the currency pair
        closeValues = fetchClosePrices(currencyIn, currencyOut)
        lastCloseValue = closeValues[-1]
        #
        mean = self.computeSimpleMeanAverage(closeValues)
        std = self.comput_standarDeviation(closeValues)
        # Compute Bollinger Bands values from close prices
        highBand = mean + (2*std)
        lowBand = mean - (2*std)
        # Strategy
        moneyStack = moneyIn / lastCloseValue
        buyValue = ((lowBand - lastCloseValue) / 10) * moneyStack
        sellValue = ((lastCloseValue - highBand) / 10) * moneyOut

        if (lastCloseValue < lowBand and moneyStack > buyValue and buyValue > 0.000001):
            # BUY
            if (pastAction):
                print(";", end='')
            self.buy(currencyIn, currencyOut, buyValue)
            return True
        elif (lastCloseValue > highBand and moneyOut > sellValue and sellValue > 0.000001):
            # SELL
            if (pastAction):
                print(";", end='')
            self.sell(currencyIn, currencyOut, sellValue)
            return True
        else:
            return False

    def strategy(self, candles: list, stack: Stack) -> None:

        action = False

        action = self.transaction(
            "BTC", "ETH", stack._BTC,
            stack._ETH, candles, action) or action

        action = self.transaction(
            "USDT", "ETH", stack._USDT,
            stack._ETH, candles, action) or action

        action = self.transaction(
            "USDT", "BTC", stack._USDT,
            stack._BTC, candles, action) or action

        if action is False:
            self.no_moves()
        else:
            # Print a RETURN character
            print()
