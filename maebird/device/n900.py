#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#ssms Ossipena/TimoP
#send smses from command line
#licence : Do whatever you want
#deps:
#pyside-qt4
#pyside-mobility
 
'''imports'''
from QtMobility.Messaging import *
import sys
from PyQt4.QtCore import QCoreApplication, QString
 
 
app = QCoreApplication(sys.argv)
 
'''get number and name'''
stringit = sys.argv
numpertemp = str(stringit[1:2])
mesits = str(stringit[2:])[2:-2]
 
num = str(numpertemp[2:-2])
 
if (mesits == ""):
    print "Usage:"
    print "python ssms.py 01234567 'message text here'"
    sys.exit(69)
else:
    print "number is " + str(num)
    print "message is " + str(mesits)
 
'''define message to be sent'''
numperi = QString(num)
 
numper = QMessageAddress(QMessageAddress.Phone, numperi)
mesitsi = QMessage()
mesitsi.setType(QMessage.Sms)
mesitsi.setTo(numper)
mesitsi.setBody(mesits)
 
'''send message'''
#sender = QMessageService()
#if (sender.send(mesitsi)):
#    print "success"
#else:
#    print "fail"