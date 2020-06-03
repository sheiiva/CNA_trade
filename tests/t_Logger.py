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


import pytest

from io import StringIO
import sys

import includes.globalDefinitions as globals
from sources.utils.Logger import Logger


def test_normalCase():
#     # Create the in-memory `file`.
#     _tmpStream = StringIO()
#     # Replace default stderr with the tempory stream file.
#     sys.stderr = _tmpStream

    Logger("Hello world!")

#     # Stock the output to remove the final '\n' of the stream.
#     output = _tmpStream.getvalue()[:-1]

#     self.assertEqual("ERROR:root:Hello world!", output)

#     # Set the standard error output to the original output.
#     sys.stderr = sys.__stderr__
#     # Close the in-memory stream
#     _tmpStream.close()