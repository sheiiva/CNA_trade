#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/21/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#


import includes.globalDefinitions as globals
from sources.utils.Logger import Logger
from sources.utils.Utilities import Utilities

# UPDATE FORMAT
CURRENCY = 0
VALUE = 1


class Stack():
    """
    Stack of money in three currencies:
        USDT, ETH, BTC
    """

    def __init__(self):
        self._USDT = 0.
        self._ETH = 0.
        self._BTC = 0.

        #
        self._utils = Utilities()

    def updateCurrency(self, currency: str, value: str) -> None:
        """
        Update Stack's currency with a given value.

        Args:
            currency (str): Currency to update.
            value (str): New value for the given currency.
        """

        if currency == "USDT":
            self._USDT = float(value)
        elif currency == "ETH":
            self._ETH = float(value)
        elif currency == "BTC":
            self._BTC = float(value)

    def update_s(self, updateCommand: str) -> None:
        """
        Update Stack's currencies from the given command.

        Args:
            updateCommand (str): Command to be parsed.
        """

        currenciesUpdate = updateCommand.split(sep=",")
        if len(currenciesUpdate) is not 3:
            Logger("Might update the three currencies.")
            return

        for currencyUpdate in currenciesUpdate:
            update = currencyUpdate.split(sep=":")
            if len(update) is not 2:
                Logger("Wrong format. Command: update_s")
            elif (update[CURRENCY] in globals.currencies) is False:
                Logger(
                    f"{update[CURRENCY]} is not a valid currency."
                    f"Currencies are {globals.currencies}"
                )
            elif self._utils.isFloat(update[VALUE]) is False:
                Logger("Wrong {} value.".format(update[CURRENCY]))
            else:
                self.updateCurrency(
                    currency=update[CURRENCY],
                    value=update[VALUE]
                )
