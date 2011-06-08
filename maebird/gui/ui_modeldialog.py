# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './maebird/gui/modeldialog.ui'
#
# Created: Thu Nov 11 20:52:27 2010
#      by: PySide uic UI code generator
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

