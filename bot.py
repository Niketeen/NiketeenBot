# -*- coding: utf-8 -*-
import config
import telebot
import metrics
import currencies
import keyboards
import commands
import time
import loggingRequests
from io import BytesIO
from PIL import Image

NiketeenBot = telebot.TeleBot(config.TelegramBotToken)

#@bot.message_handler(regexp="SOME_REGEXP")
#def handle_message(message):
#    pass

@NiketeenBot.message_handler(commands=[commands.start])
def welcome(message):
    loggingRequests.printToDisplay(message, 'Welcoming')
    NiketeenBot.send_message(message.chat.id, "Добро пожаловать в гости к тестовому боту Niketeen!", reply_markup=keyboards.mainMenu())
    metrics.track(message, 'Welcoming')
    return

@NiketeenBot.message_handler(content_types=["text"])
def answer(message):
    loggingRequests.printToDisplay(message, 'Command')
    if   message.text == commands.showTime:
        NiketeenBot.send_message(message.chat.id, "Текущее челябинское время :" + time.strftime('%X %x') + "!")
        metrics.track(message, 'timeRequest')
    elif message.text == commands.showCurrencies:
        NiketeenBot.send_message(message.chat.id, "Выберите нужную валюту:", reply_markup=keyboards.currencyMenu())
        metrics.track(message, 'currenciesRequest')
    elif message.text == commands.dollar:
        ipRates = currencies.getInvestpayDollar()
        NiketeenBot.send_message(message.chat.id, "Курс доллара согласно ЦБ: " + currencies.getDollarRate() + " руб.\nЕго можно купить в Челябинвестбанке за " + str(ipRates[1]) + " руб. или продать там же за " + str(ipRates[0]) + " руб.")
        metrics.track(message, 'dollarRateRequest')
    elif message.text == commands.euro:
        ipRates = currencies.getInvestpayEuro()
        NiketeenBot.send_message(message.chat.id, "Курс евро согласно ЦБ: " + currencies.getEuroRate() + " руб.\nЕго можно купить в Челябинвестбанке за " + str(ipRates[1]) + " руб. или продать там же за " + str(ipRates[0]) + " руб.")
        metrics.track(message, 'euroRateRequest')
    elif message.text == commands.menu:
        NiketeenBot.send_message(message.chat.id, "Выберите команду:", reply_markup=keyboards.mainMenu())
        metrics.track(message, 'menu')
    else:
        img = open('img.png', 'rb')
        NiketeenBot.send_photo(message.chat.id, img)
        NiketeenBot.send_message(message.chat.id, "Непонятная  мне команда. Попробуйте снова!")
        metrics.track(message, 'unknownCommand')
    return

if __name__ == '__main__':
     NiketeenBot.polling(none_stop=True)
