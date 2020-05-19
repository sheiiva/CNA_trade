#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/19/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#

from copy import copy

class Parser():

    """
    Main class of the Trade project.
    """

    def toList(self, string:str) -> list:

        """
        Return a list of all the words in "string".
        """

        return string.split()