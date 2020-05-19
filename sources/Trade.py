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

from sources.Parser import Parser

class Trade():

    """
    Main class of the Trade project.
    """


    def __init__(self):

        """
        Initialization of Trade Class's attributes.
        """
        self._state = True
        self._parser = Parser()

        # Run program's main loop
        self.run()

    def getInput(self) -> str:

        """
        Get input and catch potential errors.
        """

        try:
            inputs = input()
        except EOFError:
            exit(84)
        except InterruptedError:
            exit(84)
        else:
            return inputs

    def run(self) -> None:

        """
        Main loop of the Trade project.
        """

        while (self._state):
            strInput = self.getInput()
            inputs = self._parser.toList(strInput)
