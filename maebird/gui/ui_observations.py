# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/observations.ui'
#
# Created: Sun Jun 26 21:46:33 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_observationDialog(object):
    def setupUi(self, observationDialog):
        observationDialog.setObjectName("observationDialog")
        observationDialog.resize(437, 372)
        self.verticalLayout = QtGui.QVBoxLayout(observationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(observationDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 317))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sppLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sppLineEdit.setObjectName("sppLineEdit")
        self.gridLayout.addWidget(self.sppLineEdit, 0, 3, 1, 4)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.locLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.locLineEdit.setObjectName("locLineEdit")
        self.gridLayout.addWidget(self.locLineEdit, 2, 2, 1, 4)
        self.gpsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.gpsButton.setObjectName("gpsButton")
        self.gridLayout.addWidget(self.gpsButton, 2, 6, 1, 1)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 3, 1, 4)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.notesTextEdit = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesTextEdit.sizePolicy().hasHeightForWidth())
        self.notesTextEdit.setSizePolicy(sizePolicy)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout.addWidget(self.notesTextEdit, 3, 2, 1, 5)
        self.countSpinBox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countSpinBox.sizePolicy().hasHeightForWidth())
        self.countSpinBox.setSizePolicy(sizePolicy)
        self.countSpinBox.setMinimum(1)
        self.countSpinBox.setMaximum(10000)
        self.countSpinBox.setObjectName("countSpinBox")
        self.gridLayout.addWidget(self.countSpinBox, 1, 2, 1, 1)
        self.abbrLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abbrLineEdit.sizePolicy().hasHeightForWidth())
        self.abbrLineEdit.setSizePolicy(sizePolicy)
        self.abbrLineEdit.setObjectName("abbrLineEdit")
        self.gridLayout.addWidget(self.abbrLineEdit, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.firstButton = QtGui.QToolButton(observationDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image165.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstButton.setIcon(icon)
        self.firstButton.setObjectName("firstButton")
        self.gridLayout_2.addWidget(self.firstButton, 0, 0, 1, 1)
        self.prevButton = QtGui.QToolButton(observationDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/image34.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevButton.setIcon(icon1)
        self.prevButton.setObjectName("prevButton")
        self.gridLayout_2.addWidget(self.prevButton, 0, 1, 1, 1)
        self.nextButton = QtGui.QToolButton(observationDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/image39.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 0, 2, 1, 1)
        self.lastButton = QtGui.QToolButton(observationDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/image166.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastButton.setIcon(icon3)
        self.lastButton.setObjectName("lastButton")
        self.gridLayout_2.addWidget(self.lastButton, 0, 3, 1, 1)
        self.closeButton = QtGui.QPushButton(observationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 0, 4, 1, 1)
        self.saveButton = QtGui.QPushButton(observationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(observationDialog)
        QtCore.QMetaObject.connectSlotsByName(observationDialog)
        observationDialog.setTabOrder(self.abbrLineEdit, self.sppLineEdit)
        observationDialog.setTabOrder(self.sppLineEdit, self.countSpinBox)
        observationDialog.setTabOrder(self.countSpinBox, self.dateTimeEdit)
        observationDialog.setTabOrder(self.dateTimeEdit, self.locLineEdit)
        observationDialog.setTabOrder(self.locLineEdit, self.gpsButton)
        observationDialog.setTabOrder(self.gpsButton, self.notesTextEdit)
        observationDialog.setTabOrder(self.notesTextEdit, self.firstButton)
        observationDialog.setTabOrder(self.firstButton, self.prevButton)
        observationDialog.setTabOrder(self.prevButton, self.nextButton)
        observationDialog.setTabOrder(self.nextButton, self.lastButton)
        observationDialog.setTabOrder(self.lastButton, self.scrollArea)

    def retranslateUi(self, observationDialog):
        observationDialog.setWindowTitle(QtGui.QApplication.translate("observationDialog", "Observations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("observationDialog", "Spp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("observationDialog", "Loc", None, QtGui.QApplication.UnicodeUTF8))
        self.gpsButton.setText(QtGui.QApplication.translate("observationDialog", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("observationDialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEdit.setDisplayFormat(QtGui.QApplication.translate("observationDialog", "dd.MM.yyyy hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("observationDialog", "#", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setText(QtGui.QApplication.translate("observationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setText(QtGui.QApplication.translate("observationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("observationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setText(QtGui.QApplication.translate("observationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("observationDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("observationDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))

import maebird_rc
