#  B4 - COMPUTER NUMERICAL ANALYSIS
#      -----------------------
#           TRADE PROJECT
#
# Repository:
# https://github.com/sheiiva/CNA_trade
#
# (05/23/2020)
# Authors:  Corentin COUTRET-ROZET  <corentin.rozet@epitech.eu>
#           Patricia Monfa-Matas    <patricia.monfa-matas@epitech.eu>
#


import unittest

import includes.globalDefinitions as globals
from sources.Transaction import Transaction


class TestTransaction(unittest.TestCase):

    # Bind output logs.

    def test_isValidCurrency_normalCase(self):

        transaction = Transaction()

        self.assertTrue(transaction.isValidCurrency("ETH"))

    def test_isValidCurrency_wrongCase(self):

        transaction = Transaction()

        self.assertFalse(transaction.isValidCurrency("ETHH"))
