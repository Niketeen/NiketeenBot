# -*- coding: utf-8 -*-

import commands

def mainMenu():
    from telebot import types
    mainKeyboard = types.ReplyKeyboardMarkup()
    mainKeyboard.row(commands.showTime)
    mainKeyboard.row(commands.showCurrencies)
    mainKeyboard.resize_keyboard = True
    return mainKeyboard

def currencyMenu():
    from telebot import types
    currencyMenuKeyboard = types.ReplyKeyboardMarkup()
    currencyMenuKeyboard.row(commands.dollar, commands.euro)
    currencyMenuKeyboard.row(commands.menu)
    currencyMenuKeyboard.resize_keyboard = True
    return currencyMenuKeyboard
