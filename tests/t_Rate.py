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


import unittest

import includes.globalDefinitions as globals
from sources.Rate import Rate


class TestRate(unittest.TestCase):

    def test_nomalcase(self):
        
        rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(rate._state, globals.VALID)
        # self.assertEqual(rate._currency1, "USDT")
        # self.assertEqual(rate._currency2, "BTC")
        # self.assertEqual(rate._date, 1516147200)
        # self.assertEqual(rate._high, 11600.12523891)
        # self.assertEqual(rate._low, 11032.9211865)
        # self.assertEqual(rate._open, 11041.42197477)
        # self.assertEqual(rate._close, 11214.06052489)
        # self.assertEqual(rate._volume, 4123273.6568455)
