# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/infodialog.ui'
#
# Created: Sun Jun 26 21:46:33 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        infoDialog.setObjectName("infoDialog")
        infoDialog.resize(471, 373)
        self.verticalLayout = QtGui.QVBoxLayout(infoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(infoDialog)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 451, 353))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sppCommonLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.sppCommonLabel.setFont(font)
        self.sppCommonLabel.setObjectName("sppCommonLabel")
        self.verticalLayout_2.addWidget(self.sppCommonLabel)
        self.sppSciLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sppSciLabel.setCursor(QtCore.Qt.ArrowCursor)
        self.sppSciLabel.setMidLineWidth(2)
        self.sppSciLabel.setTextFormat(QtCore.Qt.RichText)
        self.sppSciLabel.setObjectName("sppSciLabel")
        self.verticalLayout_2.addWidget(self.sppSciLabel)
        self.sppSecLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sppSecLabel.setTextFormat(QtCore.Qt.RichText)
        self.sppSecLabel.setObjectName("sppSecLabel")
        self.verticalLayout_2.addWidget(self.sppSecLabel)
        self.sppTerLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sppTerLabel.setTextFormat(QtCore.Qt.RichText)
        self.sppTerLabel.setObjectName("sppTerLabel")
        self.verticalLayout_2.addWidget(self.sppTerLabel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(infoDialog)
        QtCore.QMetaObject.connectSlotsByName(infoDialog)

    def retranslateUi(self, infoDialog):
        infoDialog.setWindowTitle(QtGui.QApplication.translate("infoDialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.sppCommonLabel.setText(QtGui.QApplication.translate("infoDialog", "Common name", None, QtGui.QApplication.UnicodeUTF8))
        self.sppSciLabel.setText(QtGui.QApplication.translate("infoDialog", "Scientific name", None, QtGui.QApplication.UnicodeUTF8))
        self.sppSecLabel.setText(QtGui.QApplication.translate("infoDialog", "Secondary name", None, QtGui.QApplication.UnicodeUTF8))
        self.sppTerLabel.setText(QtGui.QApplication.translate("infoDialog", "Tertiary name", None, QtGui.QApplication.UnicodeUTF8))

