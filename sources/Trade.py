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

from enum import Enum

import includes.globalDefinitions as globals
from sources.utils.Logger import Logger
from sources.utils.Utilities import Utilities
from sources.Candle import Candle
from sources.Stack import Stack
from sources.Transaction import Transaction


class Step(Enum):
    """
    Define steps for the main loop.
    """

    END = 0
    SETTINGS = 1
    TRAINING = 2
    STRATEGY = 3


class Trade():
    """
    Main class of the Trade project.
    """

    def __init__(self):
        self._state = Step.SETTINGS
        self._settings = {}
        self._candles = []
        self._stack = Stack()

        # Attributes to other classes
        self._utils = Utilities()
        self._t = Transaction()

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
            Logger("\nexit.", logType="INFO")
            exit(0)
        else:
            return inputs

    def initSettings(self, inputs: list) -> None:
        """
        Parse the input passed as argument
        and initialise corresponding class's attribute.

        Args:
            inputs (list): Input to be parsed.
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

        if inputs[globals.VARIABLE] == "initial_stack":
            self._stack._USDT = value
        if inputs[globals.VARIABLE] == "candles_given":
            self._t._period = int(value/2)
        self._settings[inputs[globals.VARIABLE]] = value

    def fetchCommand(self, command: list) -> None:
        """
        Fetch the right command depending of the input and execute it.

        Args:
            command (list): the command to be checked and executed.
        """

        if command[0] == "settings" and len(command) is 3:
            self._state = Step.SETTINGS  # STATE USEFULL ?
            self.initSettings(command)
        elif command[0] == "update" and len(command) == 4:
            self._state = Step.TRAINING  # STATE USEFULL ?
            if f"{command[1]} {command[2]}" == "game next_candles":
                newCandle = Candle(command[3])
                if newCandle._state == globals.VALID:
                    self._candles.append(newCandle)
                    self._t.update_lastClosePrices(newCandle)
            elif f"{command[1]} {command[2]}" == "game stacks":
                self._stack.update_s(command[3])
        elif f"{command[0]} {command[1]}" == "action order":
            self._state = Step.STRATEGY  # STATE USEFULL ?
            # Server is waiting for a move. (`sell`|`buy`|`pass`)
            self._t.strategy(candles=self._candles, stack=self._stack)
        else:
            Logger("Unrecognized command.")

    def run(self) -> None:
        """
        Main loop of the Trade project.
        """

        while (self._state != Step.END):
            inputCommand = self.getInput()
            # If no input: restart loop
            if len(inputCommand) is 0:
                continue
            inputParsed = inputCommand.split()
            # Fetch to the right command
            self.fetchCommand(inputParsed)
