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
from sources.Candle import Candle


class TestCandle(unittest.TestCase):

    def test_normalCase(self):

        candle = Candle("BTC_ETH,1516147200,0.095,0.09181,0.09219501,0.09199999,481.51276914;USDT_ETH,1516147200,1090.1676815,1022.16791604,1023.1,1029.99999994,1389783.7868468;USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(candle._state, globals.VALID)

    def test_wrongRateNumber(self):

        candle = Candle("USDT_ETH,1516147200,1090.1676815,1022.16791604,1023.1,1029.99999994,1389783.7868468;USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(candle._state, globals.INVALID)

    def test_FirstRateInvalid(self):

        candle = Candle("BTC_ETH,date,0.095,0.09181,0.09219501,0.09199999,481.51276914;USDT_ETH,1516147200,1090.1676815,1022.16791604,1023.1,1029.99999994,1389783.7868468;USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(candle._state, globals.INVALID)

    def test_SecondRateInvalid(self):

        candle = Candle("BTC_ETH,1516147200,0.095,0.09181,0.09219501,0.09199999,481.51276914;USDT_ETH,date,1090.1676815,1022.16791604,1023.1,1029.99999994,1389783.7868468;USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(candle._state, globals.INVALID)

    def test_ThirdRateInvalid(self):

        candle = Candle("BTC_ETH,1516147200,0.095,0.09181,0.09219501,0.09199999,481.51276914;USDT_ETH,1516147200,1090.1676815,1022.16791604,1023.1,1029.99999994,1389783.7868468;USDT_BTC,date,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

        self.assertEqual(candle._state, globals.INVALID)
