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


import includes.globalDefinitions as globals
from sources.Utilities import Utilities
from sources.Candle import Candle

class Trade():
    """
    Main class of the Trade project.
    """

    def __init__(self):
        self._state = True
        self._settings = {}
        self._candles = []

        # Attributes to other classes
        self._utils = Utilities()

        # Run program's main loop
        self.run()

    def getInput(self) -> str:
        """
        Get input and catch potential errors.

        Returns:
            str: Input received from stdin.
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

    def initSettings(self, inputs: str) -> None:
        """
        Parse the input passed as argument
        and initialise corresponding class's attribute.

        Args:
            inputs (str): Input to be parsed.
        """

        if inputs[globals.VARIABLE] == "candle_format":
            # Candle format is set by default, don't need to stock it.
            return

        if self._utils.isInt(inputs[globals.VALUE]):
            value = int(inputs[globals.VALUE])
        elif self._utils.isFloat(inputs[globals.VALUE]):
            value = float(inputs[globals.VALUE])
        else:
            value = inputs[globals.VALUE]

        self._settings[inputs[globals.VARIABLE]] = value

    def fetchCommand(self, command: list) -> None:
        """
        Fetch the right command depending of the input and execute it.

        Args:
            command (list): the command to be checked and executed.
        """

        if command[0] == "setting":
            self.initSettings(command)
        elif command[0] == "update" and len(command) == 4:
            if f"{command[1]} {command[2]}" == "game next_candles":
                newCandle = Candle(command[3])
                if newCandle._state == globals.VALID:
                    self._candles.append(newCandle)
            elif f"{command[1]} {command[2]}" == "game stacks":
                # print("updating stack")
                pass
        else:
            # print("INPUT ERROR: Unrecognized command.")
            pass

    def run(self) -> None:
        """
        Main loop of the Trade project.
        """

        while (self._state):
            inputCommand = self.getInput()
            # If no input: restart loop
            if len(inputCommand) is 0:
                continue
            inputParsed = inputCommand.split()
            # Fetch to the right command
            self.fetchCommand(inputParsed)
