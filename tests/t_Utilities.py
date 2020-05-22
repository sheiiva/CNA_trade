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


import unittest

import includes.globalDefinitions as globals
from sources.utils.Utilities import Utilities


class TestUtilities(unittest.TestCase):

    def test_isIntNormalcase(self):

        utils = Utilities()

        self.assertTrue(utils.isInt(42))

    def test_isIntWrongcase(self):

        utils = Utilities()

        self.assertFalse(utils.isInt("Not an integer"))

    def test_isFloatNormalcase(self):

        utils = Utilities()

        self.assertTrue(utils.isFloat(42.))

    def test_isFloatWrongcase(self):

        utils = Utilities()

        self.assertFalse(utils.isFloat("Not a float"))
