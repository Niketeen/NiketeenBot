# -*- coding: utf-8 -*-

import requests
import json

URL_CURRENCY = 'http://www.cbr.ru/scripts/XML_daily_eng.asp'
URL_INVPAY_RATES = 'https://www.investpay.ru/info/currencies'

DOLLAR    = 'dollar'
DOLLAR_ID = 'R01235'
EURO    = 'euro'
EURO_ID = 'R01239'

def getCurrencies():
    cXML = requests.get(URL_CURRENCY).text
    import xml.etree.ElementTree as ET
    root = ET.fromstring(cXML)
    return root

def getCurrencyInfo(CurrencyID):
    root = getCurrencies()
    for child in root:
        if child.get('ID') == CurrencyID:
            return child
    return root

def getCurrencyRate(CurrencyID):
    root = getCurrencyInfo(CurrencyID)
    for child in root:
        if child.tag == 'Value':
             return child.text
    return root

def getDollarRate():
    return getCurrencyRate(DOLLAR_ID)

def getEuroRate():
    return getCurrencyRate(EURO_ID)

def getInvestpayRates():
    return requests.get(URL_INVPAY_RATES).json()

def getInvestpayDollar():
    rates = getInvestpayRates()
    return [rates["dollar"]["circumstances"][0]["buy"], rates["dollar"]["circumstances"][0]["sell"]]

def getInvestpayEuro():
    rates = getInvestpayRates()
    return [rates["euro"]["circumstances"][0]["buy"], rates["euro"]["circumstances"][0]["sell"]]
    
