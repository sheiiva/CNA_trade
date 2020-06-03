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

import includes.globalDefinitions as globals
from sources.utils.Utilities import Utilities


def test_isIntNormalcase():

    utils = Utilities()

    assert utils.isInt(42)


def test_isIntWrongcase():

    utils = Utilities()

    assert not utils.isInt("Not an integer")


def test_isFloatNormalcase():

    utils = Utilities()

    assert utils.isFloat(42.)


def test_isFloatWrongcase():

    utils = Utilities()

    assert not utils.isFloat("Not a float")
