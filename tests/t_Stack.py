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


import pytest
import sys
import logging

import includes.globalDefinitions as globals
from sources.Stack import Stack


def test_constructor():
    stack = Stack()

    assert stack._USDT == 0
    assert stack._ETH == 0
    assert stack._BTC == 0

def test_update_s_normalCase():
    stack = Stack()

    stack.update_s("USDT:42,ETH:21,BTC:12.1")

    assert stack._USDT == 42
    assert stack._ETH == 21
    assert stack._BTC == 12.1

def test_update_s_normalCase_other_order():
    stack = Stack()

    stack.update_s("ETH:21,USDT:42,BTC:12.1")

    assert stack._USDT == 42
    assert stack._ETH == 21
    assert stack._BTC == 12.1

def test_update_s_not_a_float():
    stack = Stack()

    stack.update_s("ETH:a,USDT:42,BTC:12.1")

    assert stack._USDT == 42
    assert stack._ETH == 0
    assert stack._BTC == 12.1

def test_update_s_wrongFormat():
    stack = Stack()

    stack.update_s("ETH;42,USDT;12.1,BTC;a")

    assert stack._USDT == 0
    assert stack._ETH == 0
    assert stack._BTC == 0

def test_update_s_wrongCurrencyFormat():
    stack = Stack()

    stack.update_s("ETH:,USDT:12.1,BTC:11")

    assert stack._USDT == 12.1
    assert stack._ETH == 0
    assert stack._BTC == 11

def test_update_s_wrongCurrency(caplog):
    stack = Stack()

    stack.update_s("None:42,USDT:12.1,BTC:1")

    assert stack._USDT == 12.1
    assert stack._ETH == 0
    assert stack._BTC == 1
     
    with caplog.at_level(logging.ERROR):
        assert caplog.records[0].message == f"None is not a valid currency."\
                                            f"Currencies are {globals.currencies}"


def test_update_s_notAllCurrencies(caplog):
    stack = Stack()

    stack.update_s("ETH:42")

    assert stack._USDT == 0
    assert stack._ETH == 0
    assert stack._BTC == 0
 
    with caplog.at_level(logging.ERROR):
        assert caplog.records[0].message == "Might update the three currencies."
