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


import includes.globalDefinitions as globals
from sources.utils.Logger import Logger
from sources.utils.Utilities import Utilities


class Rate():
    """
    A rate defines all the value of its candle for a given pair of currencies.
    """

    def __init__(self, inputRate: str):
        self._state = globals.INVALID
        self._currency1 = None
        self._currency2 = None
        self._date = 0
        self._high = 0.
        self._low = 0.
        self._open = 0.
        self._close = 0.
        self._volume = 0.

        # Run Rate's parser
        self.parseInputRate(inputRate)

    def initPair(self, inputPair: str) -> None:
        """
        Initialise the pair of currencies.

        Args:
            inputPair (str): Input string to be parsed and checked.
        """

        def isValidCurrency(inputCurrency: str) -> bool:
            if inputCurrency in globals.currencies:
                return True
            return False

        # Parse the pair of currencies
        inputPair = inputPair.split(sep="_")

        # Check the pair of currencies
        if len(inputPair) is not 2:
            Logger("Might be a pair such as `currency_currency`.")
        elif isValidCurrency(inputPair[0]) is False\
            or isValidCurrency(inputPair[1]) is False:
            Logger("Wrong currency.")
        elif inputPair[0] == inputPair[1]:
            Logger("Two times the same currency.")
        else:
            self._currency1 = inputPair[0]
            self._currency2 = inputPair[1]

    def initDate(self, inputDate: str) -> int:
        """
        Initialize the Rate's date.

        Args:
            inputDate (str): Input string to be checked.

        Returns:
            int: Return None if it cannot initialize the date.
                 Return the cast value otherwise.
        """

        if Utilities().isInt(inputDate) is False:
            Logger("Rate's date might be an integer.")
            return None

        return int(inputDate)

    def initPrice(self, inputPrice: str) -> float:
        """
        Initialize a price value of the current rate.

        Args:
            inputPrice (str): Input string to be checked.

        Returns:
            float: Return None if it cannot initialize the price.
                   Return the cast value otherwise.
        """

        if Utilities().isFloat(inputPrice) is False:
            Logger("Prices might be floats.")
            return None
        return float(inputPrice)

    def parseInputRate(self, inputRate: str):
        """
        Parse the inputRate into class' attributes.

        Args:
            inputRate (str): The input to be parsed.

        Returns:
            bool: False if it cannot initialize the Rate. True otherwise.
        """

        # Split input string (cut by a colon)
        items = inputRate.split(sep=",")
        if len(items) is not 7:
            Logger("Wrong input rate.")
            return None

        self.initPair(items[globals.CANDLE_FORMAT["PAIR"]])
        self._date = self.initDate(items[globals.CANDLE_FORMAT["DATE"]])
        self._high = self.initPrice(items[globals.CANDLE_FORMAT["HIGH"]])
        self._low = self.initPrice(items[globals.CANDLE_FORMAT["LOW"]])
        self._open = self.initPrice(items[globals.CANDLE_FORMAT["OPEN"]])
        self._close = self.initPrice(items[globals.CANDLE_FORMAT["CLOSE"]])
        self._volume = self.initPrice(items[globals.CANDLE_FORMAT["VOLUME"]])
        # Change the Rate's state to VALID if all of its attributes are valid
        if all([self._currency1, self._currency2, self._date, self._high,
                self._low, self._open, self._open, self._close, self._volume]):
            self._state = globals.VALID
