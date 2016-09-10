# -*- coding: utf-8 -*-

import time

BORDER_LINE = '*********************************************'

def printToDisplay(message, result):
    f = open('log.txt', 'a')
    mesArr = []
    mesArr.append(BORDER_LINE)
    mesArr.append('+++ New message from ' + str(message.from_user.last_name) + ' ' + str(message.from_user.first_name) + ' (id = ' + str(message.from_user.id) + ')')
    mesArr.append('+++ Time: ' + time.strftime('%X %x'))
    mesArr.append('+++ Text:')
    mesArr.append(message.text)
    mesArr.append('+++ Result:')
    mesArr.append(result)
    mesArr.append(BORDER_LINE)
    for mes in mesArr:
        print(mes)
        f.write(mes + '\n')
    f.close()
    return

