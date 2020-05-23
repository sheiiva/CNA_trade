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
            Candle("BTC_ETH,1516206600,0.0883245,0.0846429,0.08580607,0.08800513,312.13480615;USDT_ETH,1516206600,910,834.25622262,856.34533328,907.20785582,2033611.1191791;USDT_BTC,1516206600,10351.51360496,9828.00000002,10000,10349.99999999,3734703.9103735"),
            Candle("BTC_ETH,1516208400,0.088995,0.08664251,0.088015,0.0872724,339.96818419;USDT_ETH,1516208400,923.09999997,870.41373192,909.99999999,875.634585,2114090.5460197;USDT_BTC,1516208400,10400,9985,10342.07448,10059.99639994,3960575.6321135"),
            Candle("BTC_ETH,1516210200,0.08852381,0.0861,0.08728982,0.08805377,163.22932627;USDT_ETH,1516210200,902.55812307,835.20728572,875.634585,889,1522347.3680006;USDT_BTC,1516210200,10196.45349697,9800,10000.00298196,10051.49984642,4255711.8472922"),
            Candle("BTC_ETH,1516212000,0.08817192,0.08679744,0.0878658,0.08740094,208.91933787;USDT_ETH,1516212000,889,848,889,857.01299997,571303.79369559;USDT_BTC,1516212000,10083.18742211,9750,10068.06744627,9821.96433918,1578624.7881661"),
            Candle("BTC_ETH,1516213800,0.08830004,0.08701749,0.08740097,0.08736454,68.21183935;USDT_ETH,1516213800,875.00000005,849.8915823,857.013,851.8505,165482.60809516;USDT_BTC,1516213800,9987.64139727,9730,9804.75100923,9750.85525,643052.73644931"),
            Candle("BTC_ETH,1516215600,0.0883,0.08679609,0.08736454,0.08679609,17.09972167;USDT_ETH,1516215600,868,849.2354857,851.8505,865.7,48759.50284389;USDT_BTC,1516215600,9890,9621.50771184,9750.85525,9889.99999994,807043.85215192"),
            Candle("BTC_ETH,1516217400,0.0889938,0.08679608,0.08679609,0.0883,93.89809904;USDT_ETH,1516217400,942,861.35681821,865.7,924.00000003,950034.70434519;USDT_BTC,1516217400,10658.08592971,9777.37100003,9787.074,10469.99999995,2953229.3413906"),
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
