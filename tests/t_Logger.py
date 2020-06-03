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

import sys
import logging

import includes.globalDefinitions as globals
from sources.utils.Logger import Logger


def test_ERRORLevelCase(caplog):

    Logger("Hello world!")

    with caplog.at_level(logging.ERROR):
        assert caplog.records[0].message == "Hello world!"

def test_wrongLevelCase(caplog):

    Logger("Hello world!", logType='WRONGTYPE')

    with caplog.at_level(logging.ERROR):
        assert caplog.records[0].message == "Wrong logging type."
