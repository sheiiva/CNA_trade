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
from sources.Compute import Compute

## DEFINE CANDLE FORMAT
CANDLE_FORMAT  = {
    # pair:   The chart to which candle belongs.
    "PAIR":     0,
    # date:   Unix timestamp, which represents a certain date and time.
    "DATE":     1,
    # high:   The highest price traded in this candle.
    "HIGH":     2,
    # low:    The lowest price traded in this candle.
    "LOW" :     3,
    # open:   The opening price of this candle.
    "OPEN":     4,
    # close:  The closing price of this candle.
    "CLOSE":    5,
    # volume: The total volume that has been traded in this candle.
    "VOLUME":   6
}

# DEFINE INPUT FORMAT
COMMAND   = 0
VARIABLE  = 1
VALUE     = 2

class Trade():

    """
    Main class of the Trade project.
    """

    def __init__(self):

        """
        Initialization of Trade Class's attributes.
        """
        self._state = True
        self._settings = {}

        # Attributes to other classes
        self._parser = Parser()
        self._compute = Compute()

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
        except KeyboardInterrupt:
            print("\nexit.")
            exit(0)
        else:
            return inputs

    def initSettings(self, inputs) -> None:

        """
        Parse the input passed as argument
        and initialise corresponding class's attribute.
        """

        if inputs[VARIABLE] is "candle_format":
            # Candle format is set by default, don't need to stock it.
            return

        if self._compute.isInt(inputs[VALUE]):
            value = int(inputs[VALUE])
        elif self._compute.isFloat(inputs[VALUE]):
            value = float(inputs[VALUE])
        else:
            value = inputs[VALUE]

        self._settings[inputs[VARIABLE]] = value

    def run(self) -> None:

        """
        Main loop of the Trade project.
        """

        while (self._state):
            strInput = self.getInput()
            inputs = self._parser.toList(strInput)
            if len(inputs) == 0:
                continue
            if inputs[0] == "settings":
                self.initSettings(inputs)
            print(self._settings)
