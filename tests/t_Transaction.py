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
from sources.Candle import Candle

class TestTransaction(unittest.TestCase):

    # Bind output logs.

    def test_isValidCurrency_normalCase(self):

        transaction = Transaction()

        self.assertTrue(transaction.isValidCurrency("ETH"))

    def test_isValidCurrency_wrongCase(self):

        transaction = Transaction()

        self.assertFalse(transaction.isValidCurrency("ETHH"))

    def test_getClosingPrices_normalCase(self):

        transaction = Transaction()

        # Change `._n` to simplify tests.
        transaction._n = 3

        candles = [
            Candle("BTC_ETH,1516219200,0.09075,0.08738895,0.0883,0.08921392,191.335761;USDT_ETH,1516219200,975,909.1676282,924.00000003,962.49435604,1282237.7927758;USDT_BTC,1516219200,10840.99999999,10350,10468.953,10768.92744569,4549482.7666951"),
            Candle("BTC_ETH,1516221000,0.091,0.0887794,0.08932623,0.09027925,103.06952136;USDT_ETH,1516221000,996.65,944.49435604,962.49435604,995,1169925.471947;USDT_BTC,1516221000,11800,10540.00922298,10701.00000006,11023.90000003,5869606.1180224"),
            Candle("BTC_ETH,1516222800,0.09229306,0.0895,0.09039,0.09075563,219.18672545;USDT_ETH,1516222800,996.65,964.60679991,995,990.00000001,1762788.8665345;USDT_BTC,1516222800,11173.94628473,10565.00000001,11028.47418901,10899.99999986,3176851.6894339"),
            Candle("BTC_ETH,1516224600,0.0927,0.09012191,0.0914842,0.09239994,321.10136768;USDT_ETH,1516224600,1060.99877995,985,990.5,1055.00000003,1946421.3026575;USDT_BTC,1516224600,11750,10845.55000011,10899.99999987,11725.98,3953421.7861957"),
            Candle("BTC_ETH,1516226400,0.094,0.09,0.09239995,0.09119839,475.95416552;USDT_ETH,1516226400,1075,996,1055.00000003,1019.4,2738163.4159786;USDT_BTC,1516226400,11793.08,10999.99999999,11730.99,11302,9127973.011532"),
            Candle("BTC_ETH,1516228200,0.0927,0.09,0.09142738,0.0907592,187.20202469;USDT_ETH,1516228200,1050,963.055579,1019.4,979.56000012,1668904.4017084;USDT_BTC,1516228200,11500.00000001,10811.166526,11305,10959.36154234,9590619.9055415"),
            Candle("BTC_ETH,1516230000,0.09077734,0.089,0.0902025,0.09042024,391.03913012;USDT_ETH,1516230000,1014.53857185,947.99999997,988.65893444,990.00000004,2494607.092476;USDT_BTC,1516230000,11176.31348786,10642.09801453,10959.36154234,10982.89484619,5262360.6032129")
        ]

        expected = [
            [0.09119839, 0.0907592, 0.09042024],
            [1019.4, 979.56000012, 990.00000004],
            [11302, 10959.36154234, 10982.89484619] 
        ]

        ret = transaction.getLastNClosingPrices(candles)

        self.assertEqual(len(expected), len(ret))
        for i in range(len(expected)):
            self.assertListEqual(ret[i], expected[i])

    def test_computeSimpleMeanAverage_normalCase(self):

        transaction = Transaction()

        transaction._n_lastClosePrices = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]

        ret = transaction.computeSimpleMeanAverage()

        self.assertListEqual(ret, [5, 5, 5])

    def test_comput_standarDeviation_normalCase(self):

        transaction = Transaction()

        transaction._n_lastClosePrices = [
            [5, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2],
            [5, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2],
            [5, 1, 2, 1, 5, 1, 2, 1, 5, 1, 2],
        ]

        ret = transaction.comput_standarDeviation()

        self.assertListEqual(ret, [1.6663911618021237, 1.6663911618021237, 1.6663911618021237])