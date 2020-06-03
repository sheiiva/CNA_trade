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


import logging


class Logger:
    '''
    Class used for printing logs.
    May be removed before the end of the project. Good for testing
    '''

    def __init__(self, error="", logType='ERROR'):
        self._level = self.getLoggingLevel(logType)
        if self._level is not None:
            self.log(error)

    def getLoggingLevel(self, logType: str) -> str:
        """
        Define an output level for the logging.

        Args:
            logType (str): Can take value such as:
                                'CRITICAL'
                                'ERROR'
                                'WARNING'
                                'INFO'
                                'DEBUG'
                                'NOTSET'

        Returns:
            str: None if not a valid logType. Return the logType otherwise.
        """

        lvl = logging._nameToLevel.get(logType)
        if lvl is None:
            Logger(logType="ERROR", error="Wrong logging type.")
            return None

        logging.basicConfig(level=lvl)
        return lvl

    def log(self, error: str) -> None:
        """
        Log the `error` string on the current level output.

        Args:
            error (str): String to be logged out.
        """

        logging.log(level=self._level, msg=error)
