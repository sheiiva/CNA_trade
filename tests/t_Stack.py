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


import unittest

import includes.globalDefinitions as globals
from sources.Stack import Stack

class TestStack(unittest.TestCase):

    def test_constructor(self):
        stack = Stack()

        self.assertEqual(stack._USDT, 0.)
        self.assertEqual(stack._ETH, 0.)
        self.assertEqual(stack._BTC, 0.)

    def test_update_s_normalCase(self):
        stack = Stack()

        stack.update_s("USDT:42,ETH:21,BTC:12.1")

        self.assertEqual(stack._USDT, 42.)
        self.assertEqual(stack._ETH, 21.)
        self.assertEqual(stack._BTC, 12.1)

    def test_update_s_normalCase_other_order(self):
        stack = Stack()

        stack.update_s("ETH:21,USDT:42,BTC:12.1")

        self.assertEqual(stack._USDT, 42.)
        self.assertEqual(stack._ETH, 21.)
        self.assertEqual(stack._BTC, 12.1)

    def test_update_s_not_a_float(self):
        stack = Stack()

        stack.update_s("ETH:a,USDT:42,BTC:12.1")

        self.assertEqual(stack._USDT, 42.)
        self.assertEqual(stack._ETH, 0.)
        self.assertEqual(stack._BTC, 12.1)

    def test_update_s_wrongFormat(self):
        stack = Stack()

        stack.update_s("ETH;42,USDT;12.1,BTC;a")

        self.assertEqual(stack._USDT, 0)
        self.assertEqual(stack._ETH, 0)
        self.assertEqual(stack._BTC, 0)

    def test_update_s_wrongCurrencyFormat(self):
        stack = Stack()

        stack.update_s("ETH:,USDT:12.1,BTC:11")

        self.assertEqual(stack._USDT, 12.1)
        self.assertEqual(stack._ETH, 0)
        self.assertEqual(stack._BTC, 11)

    def test_update_s_wrongCurrency(self):
        stack = Stack()

        stack.update_s("ETHH:42,USDT:12.1,BTC:1")

        self.assertEqual(stack._USDT, 12.1)
        self.assertEqual(stack._ETH, 0)
        self.assertEqual(stack._BTC, 1.)
