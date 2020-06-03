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
import logging

import includes.globalDefinitions as globals
from sources.Rate import Rate


def test_normalCase():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.VALID
    assert rate._currency1 == "USDT"
    assert rate._currency2 == "BTC"
    assert rate._date == 1516147200
    assert rate._high == 11600.12523891
    assert rate._low == 11032.9211865
    assert rate._open == 11041.42197477
    assert rate._close == 11214.06052489
    assert rate._volume == 4123273.6568455

def test_wrongFormat():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489")

    assert rate._state == globals.INVALID

def test_wrongPairFormat():

    rate = Rate("USDT-BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongPairFirstIsNotValidCurrency():

    rate = Rate("WRONG_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongPairSecondIsNotValidCurrency():

    rate = Rate("USDT_WRONG,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongDate():

    rate = Rate("USDT_BTC,date,11600.12523891,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongHighValue():

    rate = Rate("USDT_BTC,1516147200,high,11032.9211865,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongLowValue():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,low,11041.42197477,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongOpenValue():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,open,11214.06052489,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongCloseValue():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,close,4123273.6568455")

    assert rate._state == globals.INVALID

def test_wrongVolumeValue():

    rate = Rate("USDT_BTC,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,volume")

    assert rate._state == globals.INVALID

def test_twiceSameCurrency(caplog):

    rate = Rate("USDT_USDT,1516147200,11600.12523891,11032.9211865,11041.42197477,11214.06052489,volume")

    assert rate._state == globals.INVALID

    with caplog.at_level(logging.ERROR):
        assert caplog.records[0].message == "Two times the same currency."
