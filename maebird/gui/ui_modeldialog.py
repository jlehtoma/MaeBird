# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/modeldialog.ui'
#
# Created: Sun Jun 26 21:46:33 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_modelDialog(object):
    def setupUi(self, modelDialog):
        modelDialog.setObjectName("modelDialog")
        modelDialog.resize(255, 200)
        self.verticalLayout = QtGui.QVBoxLayout(modelDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modelListWidget = QtGui.QListWidget(modelDialog)
        self.modelListWidget.setObjectName("modelListWidget")
        self.verticalLayout.addWidget(self.modelListWidget)

        self.retranslateUi(modelDialog)
        QtCore.QMetaObject.connectSlotsByName(modelDialog)

    def retranslateUi(self, modelDialog):
        modelDialog.setWindowTitle(QtGui.QApplication.translate("modelDialog", "Choose table", None, QtGui.QApplication.UnicodeUTF8))

